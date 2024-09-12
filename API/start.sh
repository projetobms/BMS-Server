#!/bin/bash

# Iniciar o daemon
python daemon.py &

# Aguardar 1 minuto (60 segundos)
sleep 60

# Iniciar o servidor FastAPI
uvicorn main:app --host 0.0.0.0 --port 8000
