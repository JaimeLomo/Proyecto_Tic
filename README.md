# 📊 Proyecto de Benchmark: VM vs Docker con Servidor Pacman

Este proyecto compara el rendimiento entre una 🖥️ Máquina Virtual (VirtualBox) y un 🐋 Contenedor Docker, ejecutando un servidor Pacman en Python con interfaz web.

---

## ⚡ Tecnologías Comparadas

### 🖥️ Máquinas Virtuales (VM)

**¿Qué es?**  
Una VM es un sistema operativo completo que se ejecuta sobre un hipervisor (como VirtualBox).

**✔️ Ventajas:**
- 🔒 Aislamiento y seguridad elevados  
- 💻 Compatibilidad con múltiples SO  
- 🛠️ Ideal para kernels personalizados  

**❌ Desventajas:**
- 🐢 Mayor consumo de recursos (CPU, RAM, disco)  
- ⏳ Inicio más lento  

---

### 🐋 Contenedores Docker

**¿Qué es?**  
Tecnología ligera que comparte el kernel del host pero aísla procesos.

**✔️ Ventajas:**
- ⚡ Uso eficiente de recursos  
- 🚀 Inicio casi instantáneo (~1 segundo)  
- 📦 Portabilidad y escalabilidad sencilla  

**❌ Desventajas:**
- 🔓 Menor aislamiento (kernel compartido)  
- ⚠️ Limitado a sistemas compatibles  

---

## 🔧 Entorno de Pruebas

| Componente | Especificaciones |
|-----------|------------------|
| **Host** | Windows 10/11, 16GB RAM, Ryzen 7 |
| **VM (VirtualBox)** | Ubuntu 22.04, 4GB RAM, 2 vCPUs |
| **Docker** | Imagen `python:3.10-slim`, 2 CPUs asignadas |
| **Aplicación** | Servidor Pacman (Python HTTP) |

---

## 📂 Estructura del Proyecto

PROYECTO_TIC/  
├── pacman/  
│   ├── vm_vs_docker_benchmark/  
│   │   ├── 📊 notebooks/  
│   │   │   ├── pacman_benchmark_comparison.ipynb  # Análisis con gráficos  
│   │   │   └── vm_vs_docker_comparison.ipynb      # Visualización de datos  
│   │   ├── 📁 results/  
│   │   │   ├── benchmark_pacman_docker.csv        # Datos Docker  
│   │   │   └── benchmark_pacman_vm.csv            # Datos VM  
│   │   ├── 🛠️ scripts/  
│   │   │   ├── benchmark_pacman.py                # Script de métricas  
│   │   │   ├── docker_setup.sh                    # Config Docker  
│   │   │   └── vm_setup_windows.sh                # Config VM  
│   │   ├── 🐋 Dockerfile                          # Imagen Docker  
│   │   └── ⚡ run_benchmark.sh                    # Ejecución automática  
├── 📚 docs/  
│   ├── presentacion.md                           # Resumen ejecutivo  
│   └── memoria_tecnica.pdf                       # Detalles técnicos  
└── 📌 README.md                                  # Guía del proyecto  

## 📊 Métricas Evaluadas

El script `benchmark_pacman.py` mide:

- 🖥️ **CPU (%)**: Uso promedio durante la ejecución.  
- 🧠 **RAM (%)**: Consumo de memoria.  
- 🌐 **Latencia (bytes)**: Tráfico de red generado.  
- 💾 **Disco (MB)**: Espacio utilizado.  

---

## 🚀 Cómo Ejecutar el Proyecto

1. 🔄 Configuración Inicial
bash
# Instalar dependencias (solo una vez)  
./scripts/docker_setup.sh       # Para Docker  
./scripts/vm_setup_windows.sh   # Para VM  
2. ⏱️ Ejecutar Benchmark
bash
# Ejecuta ambos tests (VM y Docker)  
./scripts/benchmark_pacman.py   # Para Docker
./scripts/benchmark_pacman.py --vm  # Para VM 
3. 🎮 Iniciar Servidor Pacman
bash
cd pacman_game  
python -m http.server 8000  
🔗 Abrir en navegador: http://localhost:8000


📈 Resultados y Análisis
Los datos se guardan en results/ y pueden visualizarse con:

bash
Copiar
Editar
jupyter notebook notebooks/pacman_benchmark_comparison.ipynb
📌 Ejemplo de Comparativa
Métrica	VM	Docker
CPU (%)	45.2	32.1
RAM (%)	60.0	48.3
⏱️ Tiempo inicio	15s	1.2s

🔍 Conclusiones
🐋 Docker es mejor para:
🚀 Desarrollo rápido

⚡ Microservicios y CI/CD

💡 Entornos con recursos limitados

🖥️ VM es mejor para:
🔒 Aislamiento completo

🛠️ Sistemas con kernel personalizado

📚 Recursos
Docker Docs

VirtualBox Manual

Python HTTP Server

🧑‍💻 Autores
Jaime Lomo

📌 Notas Finales
Este proyecto demuestra cómo 🐋 Docker ofrece mayor eficiencia, mientras que 🖥️ VM proporciona mejor aislamiento.

❓ ¿Preguntas? ¡Abre un issue en el repositorio!

📜 Licencia: MIT
🔗 Repositorio: GitHub

🎮 ¡Gracias por leer! 🚀