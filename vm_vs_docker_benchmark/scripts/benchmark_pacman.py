#!/usr/bin/env python

import os
import psutil
import time
import csv
import argparse
from datetime import datetime

# Configuración
DURATION = 60  # Duración del benchmark en segundos
OUTPUT_DIR = "../results/"
FILENAME_VM = "benchmark_pacman_vm"
FILENAME_DOCKER = "benchmark_pacman_docker"
HISTORICAL_DATA = False  # Cambiar a True si quieres guardar histórico

# Argumentos para automatizar entorno (sin input manual)
parser = argparse.ArgumentParser()
parser.add_argument("--vm", action="store_true", help="Especificar si el benchmark corre en una VM")
args = parser.parse_args()

filename_base = FILENAME_VM if args.vm else FILENAME_DOCKER

# Configuración de nombres de archivo
if HISTORICAL_DATA:
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{filename_base}_{timestamp}.csv"  # Archivo con timestamp
else:
    filename = f"{filename_base}.csv"  # Mismo archivo siempre

output_path = os.path.join(OUTPUT_DIR, filename)

# Variables de monitoreo
cpu_data, ram_data, latency_data = [], [], []
disk_usage = psutil.disk_usage('/').used / (1024 * 1024)  # MB

print(f"\n🔧 Ejecutando benchmark durante {DURATION} segundos...")
start_time = time.time()

while time.time() - start_time < DURATION:
    cpu_data.append(psutil.cpu_percent(interval=1))
    ram_data.append(psutil.virtual_memory().percent)
    latency_data.append(psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv)

# Resultados
avg_cpu = sum(cpu_data) / len(cpu_data)
avg_ram = sum(ram_data) / len(ram_data)
latency = max(latency_data) - min(latency_data)

# Escribir resultados
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Modo de apertura del archivo (append o write)
file_mode = 'a' if os.path.exists(output_path) and not HISTORICAL_DATA else 'w'

with open(output_path, file_mode, newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Escribir encabezado solo si es un archivo nuevo
    if file_mode == 'w':
        writer.writerow(["timestamp", "cpu", "ram", "latency", "disk_MB"])
    
    # Escribir datos
    writer.writerow([
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        round(avg_cpu, 2),
        round(avg_ram, 2),
        round(latency, 2),
        round(disk_usage, 2)
    ])

print(f"\n✅ RESUMEN DEL BENCHMARK - {'VM' if args.vm else 'Docker'}")
print(f"CPU promedio: {round(avg_cpu, 2)}%")
print(f"RAM promedio: {round(avg_ram, 2)}%")
print(f"Latencia estimada: {round(latency, 2)} bytes")
print(f"Uso de disco: {round(disk_usage, 2)} MB")
print(f"Archivo guardado en: {output_path}")