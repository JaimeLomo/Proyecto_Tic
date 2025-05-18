#!/bin/bash

SCRIPT_DIR="scripts/"
DATE=$(date +"%Y-%m-%d_%H-%M-%S")

# Ejecutar benchmark en VM
echo "🔍 Benchmark en VM iniciado a $(date)"
(cd $SCRIPT_DIR && python benchmark_pacman.py --vm > ../results/vm_log_$DATE.txt 2>&1) &

# Ejecutar benchmark en Docker
echo "🐳 Benchmark en Docker iniciado a $(date)"
(cd $SCRIPT_DIR && python benchmark_pacman.py > ../results/docker_log_$DATE.txt 2>&1) &

wait
echo "✅ Benchmarks completados. Resultados en 'results/'"
