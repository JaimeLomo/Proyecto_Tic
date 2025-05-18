#!/bin/bash

# 1. Configuración inicial
echo "🔧 Preparando entorno Docker..."
sudo apt update
sudo apt install -y python3 python3-pip psutil
pip3 install psutil

# 2. Crear directorio de resultados
mkdir -p ../results/docker

# 3. Iniciar Pacman (EN SEGUNDO PLANO)
echo "🎮 Iniciando Pacman en http://localhost:8000 ..."
cd ../pacman_game
python3 -m http.server 8000 &  # El '&' es clave
SERVER_PID=$!  # Guardamos el ID del proceso
sleep 2  # Esperamos 2 segundos para que el servidor arranque

# 4. Verificar que el servidor funciona
if ! curl -s http://localhost:8000 >/dev/null; then
    echo "❌ Error: El servidor no responde"
    kill $SERVER_PID
    exit 1
fi

# 5. Ejecutar benchmark (desde la carpeta scripts)
echo "📊 Ejecutando benchmark..."
cd ../scripts
python3 benchmark_pacman.py

# 6. Detener el servidor al finalizar
kill $SERVER_PID
echo "✅ Benchmark completado. Resultados en ../results/docker/"