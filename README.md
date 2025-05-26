# 📊 Análisis Comparativo de Rendimiento: Docker vs Máquina Virtual con Servidor Pacman

## 🔍 Introducción

Este proyecto tiene como objetivo principal evaluar el rendimiento relativo entre un entorno basado en **Máquina Virtual (VirtualBox)** y un **contenedor Docker**, ambos utilizados para desplegar un pequeño servidor HTTP que aloja el clásico juego de **Pacman**. El servidor está implementado en Python y expone una interfaz web interactiva.

La comparación se centra en medir indicadores clave de eficiencia y uso de recursos como la CPU, la memoria RAM, los tiempos de arranque y la latencia del servidor, con el fin de identificar cuál tecnología ofrece un entorno más ligero, rápido y escalable para despliegues web sencillos.

---

## 🖥️ Máquinas Virtuales vs 🐋 Contenedores Docker

### Máquinas Virtuales (VM)

**Definición:**  
Una Máquina Virtual emula un sistema operativo completo y corre sobre un hipervisor. En este proyecto se ha utilizado VirtualBox para gestionar una VM con Ubuntu 22.04.

**Ventajas:**
- Mayor aislamiento y seguridad entre el host y la VM.
- Posibilidad de ejecutar distintos sistemas operativos en paralelo.
- Ideal para pruebas que requieren modificación del kernel o acceso profundo al sistema operativo.

**Desventajas:**
- Consumo elevado de recursos del sistema.
- Tiempos de arranque y despliegue más largos.
- Overhead por la virtualización completa del hardware.

---

### Contenedores Docker

**Definición:**  
Los contenedores Docker permiten ejecutar aplicaciones en entornos ligeros que comparten el kernel del sistema anfitrión, lo que reduce significativamente la sobrecarga.

**Ventajas:**
- Uso más eficiente de recursos como CPU y memoria.
- Despliegue ultrarrápido (habitualmente inferior a 2 segundos).
- Portabilidad sencilla entre distintos entornos y sistemas operativos compatibles.

**Desventajas:**
- Menor nivel de aislamiento respecto al sistema anfitrión.
- No permite personalizaciones a bajo nivel del sistema operativo.


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
└── README.md                                          # Guía principal del proyecto
```

## ⚙️ Entorno de Pruebas

| Componente             | Especificación                                  |
|------------------------|--------------------------------------------------|
| Sistema Host           | Windows 11 Pro                                   |
| Procesador             | AMD Ryzen 7 5800X                                |
| RAM                    | 16GB DDR4                                        |
| Tarjeta Gráfica        | NVIDIA RTX 4060                                  |
| Máquina Virtual        | Ubuntu 22.04, 2 vCPUs, 4GB RAM                   |
| Contenedor Docker      | python:3.10-slim, 2 CPUs                         |
| Aplicación             | Servidor HTTP que aloja Pacman en HTML/JS       |

---

# 🧪 Cómo Ejecutar el Benchmark

## 1. Configuración

### Docker:

./scripts/docker_setup.sh

VM:
---
./scripts/vm_setup.sh
---
2. Ejecución del Benchmark
Para Docker:
---
python scripts/benchmark_pacman.py
---
Para VM:
---
python scripts/benchmark_pacman.py --vm
---
3. Visualización de Resultados
---
jupyter notebook notebooks/pacman_benchmark_comparasion.ipynb
---
📊 Métricas Analizadas

Métrica	Descripción
Uso de CPU (%)	Uso promedio del procesador durante la ejecución
Consumo de RAM (%)	Porcentaje de memoria utilizado
Latencia (ms)	Tiempo de respuesta del servidor
Tiempo de arranque	Tiempo desde el lanzamiento hasta disponibilidad

📈 Resultados (Ejemplo)
Métrica	Docker	VM	Diferencia
CPU (%)	28.5	45.2	-16.7 %
RAM (%)	42.7	60.0	-17.3 %
Latencia (ms)	87	112	-25 ms
Arranque (s)	1.5	15	-13.5 s

📂 Datos almacenados en:

results/benchmark_pacman_docker.csv

results/benchmark_pacman_vm.csv

📚 Requisitos
Instalar dependencias necesarias:
---
pip install -r requirements.txt
---
Contenido de requirements.txt:
---
nginx
Copiar
Editar
nginx
psutil
pandas
matplotlib
requests
---
🧠 Conclusiones
Docker proporciona un entorno más eficiente y ligero en términos de uso de CPU y RAM.

La latencia es menor y los tiempos de arranque mucho más rápidos en Docker.

Las Máquinas Virtuales siguen siendo útiles cuando se requiere mayor aislamiento o un sistema operativo distinto.

<<<<<<< HEAD

=======
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
