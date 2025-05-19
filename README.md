# 📊 Proyecto de Benchmark: VM vs Docker con Servidor Pacman

## 🔍 Introducción
Este proyecto compara el rendimiento entre una Máquina Virtual (VirtualBox) y un Contenedor Docker, ejecutando un servidor Pacman desarrollado en Python con interfaz web interactiva. El objetivo es evaluar las diferencias en consumo de recursos, rendimiento y facilidad de despliegue entre ambas tecnologías.

## 🖥️ vs 🐋: Comparativa Tecnológica

### 🖥️ Máquinas Virtuales (VM)

**Definición:**  
Emulación completa de un sistema operativo que se ejecuta sobre un hipervisor (VirtualBox en este caso).

**Ventajas:**
- 🔒 Aislamiento completo y mayor seguridad
- 💻 Capacidad para ejecutar diferentes sistemas operativos
- 🛠️ Entorno ideal para pruebas que requieren kernel personalizado

**Desventajas:**
- 🐢 Mayor consumo de recursos (CPU, RAM, almacenamiento)
- ⏳ Tiempos de arranque más prolongados

### 🐋 Contenedores Docker

**Definición:**  
Tecnología ligera que comparte el kernel del host pero aísla procesos y dependencias.

**Ventajas:**
- ⚡ Eficiencia extrema en uso de recursos
- 🚀 Inicio casi instantáneo (1-2 segundos)
- 📦 Portabilidad absoluta entre sistemas

**Desventajas:**
- 🔓 Menor nivel de aislamiento
- ⚠️ Limitaciones en personalización del sistema

## ⚙️ Entorno de Pruebas

| Componente         | Especificaciones Técnicas                            |
|--------------------|------------------------------------------------------|
| Sistema Host       | Windows 11 Pro, AMD Ryzen 7 5800X, 16GB RAM          |
| Configuración VM   | Ubuntu 22.04 LTS, 4GB RAM asignados, 2 vCPUs         |
| Configuración Docker | Imagen oficial `python:3.10-slim`, 2 CPUs asignadas |
| Aplicación         | Servidor HTTP Pacman (Python 3.10)                   |

## 📂 Estructura del Proyecto

```plaintext
PROYECTO_TIC/
├── pacman/
│   ├── vm_vs_docker_benchmark/
│   │   ├── notebooks/
│   │   │   ├── pacman_benchmark_comparison.ipynb     # Análisis comparativo de rendimiento
│   │   │   └── vm_vs_docker_comparison.ipynb         # Visualización de datos comparativos
│   │   ├── results/
│   │   │   ├── benchmark_pacman_docker.csv           # Resultados de ejecución en Docker
│   │   │   └── benchmark_pacman_vm.csv               # Resultados de ejecución en VM
│   │   ├── scripts/
│   │   │   ├── benchmark_pacman.py                   # Script principal de medición de rendimiento
│   │   │   ├── docker_setup.sh                       # Script para configurar entorno en Docker
│   │   │   └── vm_setup_windows.sh                   # Script para configurar entorno en Máquina Virtual
│   │   ├── Dockerfile                                # Definición de la imagen Docker
│   │   └── run_benchmark.sh                          # Script de ejecución automatizada del benchmark
├── docs/
│   ├── presentacion.md                               # Presentación ejecutiva del proyecto
│   └── memoria_tecnica.pdf                           # Documentación técnica detallada
└── README.md                                         # Guía principal del proyecto


## 📊 Métricas Evaluadas

El sistema de benchmark mide cuatro aspectos clave:

- 🖥️ **Uso de CPU (%):** Promedio de utilización del procesador durante la ejecución
- 🧠 **Consumo de Memoria (%):** Porcentaje de RAM utilizada por la aplicación
- 🌐 **Latencia de Red (bytes):** Tráfico de red generado durante las pruebas
- 💾 **Uso de Disco (MB):** Espacio en disco requerido por cada solución

## 🚀 Guía de Implementación

### 1. Configuración Inicial

```bash
# Configurar entorno Docker
./scripts/docker_setup.sh

# Configurar máquina virtual
./scripts/vm_setup_windows.sh
2. Ejecución de Benchmarks
bash
Copiar
Editar
# Para Docker (sin parámetros)
python benchmark_pacman.py

# Para VM (con flag --vm)
python benchmark_pacman.py --vm
3. Inicio del Servidor
bash
Copiar
Editar
cd pacman_game
python -m http.server 8000
Accede al juego en: http://localhost:8000

📈 Análisis de Resultados
Los datos recopilados se organizan automáticamente en:

results/benchmark_pacman_docker.csv

results/benchmark_pacman_vm.csv

Para visualizar los resultados:

bash
Copiar
Editar
jupyter notebook notebooks/pacman_benchmark_comparison.ipynb
📊 Ejemplo de Datos Obtenidos
Métrica	VirtualBox	Docker	Diferencia
CPU promedio	45.2%	32.1%	-13.1%
RAM promedio	60.0%	48.3%	-11.7%
Tiempo inicio	15s	1.2s	-13.8s

🔍 Conclusiones Clave
🐋 Ventajas de Docker
Eficiencia: 30-40% menos consumo de recursos

Velocidad: Inicio 10x más rápido

Portabilidad: Fácil despliegue en cualquier sistema

🖥️ Ventajas de VirtualBox
Seguridad: Aislamiento completo del sistema

Compatibilidad: Soporte para diferentes kernels

Control: Mayor personalización del entorno

📚 Recursos Adicionales
Documentación Oficial de Docker

Manual de VirtualBox

Python HTTP Server

👥 Autores
Jaime Lomo - Desarrollo y benchmarking