#!/bin/bash
echo "🚀 Setting up VM environment for benchmarking..."

# Instalar dependencias
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip sysbench git curl procps

# Librerías Python
pip3 install --upgrade pip
pip3 install jupyter matplotlib psutil

# Crear directorio de resultados
mkdir -p ../results/vm

# Ejecutar benchmark en segundo plano
echo "🔍 Running benchmark in background..."
python3 ../scripts/benchmark_pacman.py --vm > ../results/vm/benchmark_results_$(date +"%Y-%m-%d_%H-%M-%S").csv 2>&1 &

# Levantar servidor de juego
echo "🎮 Starting Pac-Man game server..."
cd ../pacman_game
python3 -m http.server 8000

# Esperar a que ambos procesos terminen (opcional)
wait