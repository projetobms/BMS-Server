#!/bin/bash

# Iniciar o daemon
python daemon.py &

# Iniciar o servidor FastAPI
uvicorn main:app --host 0.0.0.0 --port 8000
