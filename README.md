# 🕹️ Proyecto TIC — Benchmark de Pac-Man: VM vs Docker

Este proyecto forma parte del análisis comparativo entre entornos virtualizados mediante **VirtualBox (VM)** y **Docker**, usando como base el juego clásico **Pac-Man**. El objetivo es medir el rendimiento de ambas tecnologías ejecutando el mismo escenario.

---

## 📁 Estructura del Proyecto

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
📊 Métricas Evaluadas
El sistema de benchmark mide cuatro aspectos clave:

🖥️ Uso de CPU (%): Promedio de utilización del procesador durante la ejecución

🧠 Consumo de Memoria (%): Porcentaje de RAM utilizada por la aplicación

🌐 Latencia de Red (bytes): Tráfico de red generado durante las pruebas

💾 Uso de Disco (MB): Espacio en disco requerido por cada solución

🚀 Guía de Implementación
1. Configuración Inicial
bash
Copiar
Editar
# Configurar entorno Docker
./scripts/docker_setup.sh

# Configurar máquina virtual (Windows)
./scripts/vm_setup_windows.sh
2. Ejecución de Benchmarks
bash
Copiar
Editar
# Ejecutar en Docker
python benchmark_pacman.py

# Ejecutar en VM
python benchmark_pacman.py --vm
3. Inicio del Servidor de Juego
bash
Copiar
Editar
cd pacman_game
python -m http.server 8000
Accede al juego en tu navegador: http://localhost:8000

📈 Análisis de Resultados
Los resultados se guardan automáticamente en:

results/benchmark_pacman_docker.csv

results/benchmark_pacman_vm.csv

Para visualizar y analizar los datos:

bash
Copiar
Editar
jupyter notebook notebooks/pacman_benchmark_comparison.ipynb
📊 Ejemplo de Datos Obtenidos
Métrica	VirtualBox	Docker	Diferencia
CPU promedio	45.2%	32.1%	-13.1%
RAM promedio	60.0%	48.3%	-11.7%
Tiempo de inicio	15s	1.2s	-13.8s

🔍 Conclusiones Clave
🐋 Docker
✅ Eficiencia: 30–40% menos consumo de recursos

✅ Velocidad: Inicio 10 veces más rápido

✅ Portabilidad: Funciona en cualquier sistema con Docker instalado

🖥️ VirtualBox
🔒 Seguridad: Aislamiento total del sistema anfitrión

🧩 Compatibilidad: Soporte para múltiples sistemas operativos

⚙️ Control: Mayor nivel de personalización del entorno

📚 Recursos Adicionales
Documentación Oficial de Docker

Manual de VirtualBox

Python HTTP Server

👥 Autor
Jaime Lomo – Desarrollo y benchmarking