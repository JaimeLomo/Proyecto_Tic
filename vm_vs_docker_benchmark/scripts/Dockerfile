# Usa imagen base de Python
FROM python:3.10-slim

# Instala utilidades necesarias
RUN apt update && apt install -y sysbench git curl procps \
    && pip install --upgrade pip \
    && pip install jupyter matplotlib psutil

# Copia el proyecto completo
WORKDIR /app
COPY . .

# Puerto para el juego
EXPOSE 8000

# Ir a la carpeta del juego y levantar servidor web
WORKDIR /app/pacman_game
CMD ["python3", "-m", "http.server", "8000"]
