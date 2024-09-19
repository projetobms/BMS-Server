#!/bin/bash
# Inicie todos os scripts em paralelo
python esp_tcp_server.py &
python receive_tcp_server.py 

# Aguarde todos os processos filhos terminarem
wait
