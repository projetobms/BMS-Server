import asyncio
import websockets
from PIL import Image
from io import BytesIO
import numpy as np
import cv2

async def receive_frames(uri):
    async with websockets.connect(uri) as websocket:
        while True:
            try:
                # Receber bytes da imagem
                frame_data = await websocket.recv()
                
                # Converter bytes para uma imagem
                image = Image.open(BytesIO(frame_data))
                
                # Converter para um array numpy
                frame_array = np.array(image)
                
                # Converter a imagem para o formato que o OpenCV pode mostrar
                frame_bgr = cv2.cvtColor(frame_array, cv2.COLOR_RGB2BGR)
                
                # Mostrar a imagem
                cv2.imshow("Webcam Stream", frame_bgr)
                
                # Pressione 'q' para sair
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            except Exception as e:
                print(f"Erro: {e}")
                break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    uri = "ws://localhost:8000/ws"  # Substitua pelo endereço do seu servidor
    asyncio.run(receive_frames(uri))
