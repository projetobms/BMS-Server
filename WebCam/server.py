from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List
import cv2
import numpy as np
import asyncio
from fastapi.responses import StreamingResponse, FileResponse
import os
from datetime import datetime, timedelta
import subprocess
import sqlite3

app = FastAPI()

# Lista de conexões WebSocket
connections: List[WebSocket] = []

# Variáveis globais para o streaming de vídeo
latest_frame: bytes = b''
video_writer = None
frame_number = 0
start_time = datetime.now()
segment_duration = timedelta(minutes=1)  # Duração do segmento de vídeo
fps = 2  # Frames por segundo para o vídeo

# Diretório para salvar os vídeos e concatenar
SAVE_DIR = 'saved_videos'
os.makedirs(SAVE_DIR, exist_ok=True)

# Banco de dados SQLite
DB_FILE = 'videos.db'

def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS videos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL,
                start_time TIMESTAMP NOT NULL,
                end_time TIMESTAMP NOT NULL
            )
        ''')
        conn.commit()

def insert_video_record(filename, start_time, end_time):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO videos (filename, start_time, end_time)
            VALUES (?, ?, ?)
        ''', (filename, start_time, end_time))
        conn.commit()

def get_video_records():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT filename, start_time, end_time FROM videos ORDER BY start_time')
        return cursor.fetchall()

@app.on_event("startup")
async def startup_event():
    init_db()
    asyncio.create_task(video_stream())

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connections.append(websocket)
    try:
        while True:
            data = await websocket.receive_bytes()
            for connection in connections:
                if connection is not websocket:
                    await connection.send_bytes(data)
    except WebSocketDisconnect:
        connections.remove(websocket)

@app.get("/")
async def video_feed():
    def generate():
        global latest_frame
        while True:
            if latest_frame:
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + latest_frame + b'\r\n')
            else:
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + b'\r\n')
            asyncio.sleep(0.1)
    
    return StreamingResponse(generate(), media_type="multipart/x-mixed-replace; boundary=frame")

def save_frame_to_video(frame):
    global video_writer, frame_number, start_time

    current_time = datetime.now()
    if video_writer is None or (current_time - start_time) >= segment_duration:
        if video_writer is not None:
            video_writer.release()

        # Novo nome de arquivo com timestamp
        video_filename = os.path.join(SAVE_DIR, f"video_{current_time.strftime('%Y%m%d_%H%M%S')}.avi")
        # Configurar o VideoWriter com FPS correto
        video_writer = cv2.VideoWriter(video_filename, cv2.VideoWriter_fourcc(*'XVID'), fps, (frame.shape[1], frame.shape[0]))
        start_time = current_time

        # Adicionar entrada no banco de dados
        insert_video_record(video_filename, start_time, start_time + segment_duration)

    video_writer.write(frame)

async def video_stream():
    global latest_frame, video_writer

    captura = cv2.VideoCapture(0)
    if not captura.isOpened():
        print("Erro ao abrir a webcam.")
        return

    while True:
        ret, frame = captura.read()
        if not ret:
            break

        _, buffer = cv2.imencode('.jpg', frame)
        latest_frame = buffer.tobytes()

        save_frame_to_video(frame)

        for connection in connections:
            try:
                await connection.send_bytes(latest_frame)
            except WebSocketDisconnect:
                connections.remove(connection)

        await asyncio.sleep(1 / fps)

    captura.release()
    if video_writer is not None:
        video_writer.release()

@app.get("/concatenate_videos")
async def concatenate_videos():
    # Nome do arquivo de vídeo concatenado
    concatenated_filename = os.path.join(SAVE_DIR, "concatenated_video.avi")

    # Obter vídeos do banco de dados
    video_records = get_video_records()

    # Crie um arquivo temporário de lista de arquivos
    file_list = os.path.join(SAVE_DIR, "file_list.txt")
    with open(file_list, 'w') as f:
        for filename, _, _ in video_records:
            f.write(f"file '{os.path.join(SAVE_DIR, filename)}'\n")

    # Executar o comando FFmpeg para concatenar os vídeos
    command = [
        'ffmpeg', '-f', 'concat', '-safe', '0', '-i', file_list, '-c', 'copy', concatenated_filename
    ]
    subprocess.run(command, check=True)

    # Remover o arquivo temporário de lista
    os.remove(file_list)

    return FileResponse(concatenated_filename, media_type='video/avi', headers={'Content-Disposition': f'attachment; filename="concatenated_video.avi"'})

@app.get("/view_videos")
async def view_videos():
    video_records = get_video_records()
    video_files = [filename for filename, _, _ in video_records]
    return StreamingResponse(iter(video_files), media_type='text/plain')
