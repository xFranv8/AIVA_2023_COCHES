# Establece la imagen base de python 3.10
FROM python:3.10

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6   -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo en /code
WORKDIR /code

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias necesarias para tu aplicación
RUN pip install -r requirements.txt

# Copia todo el contenido del directorio actual a /code en el contenedor
COPY development /code/development

# Cambia al directorio WebApplication
WORKDIR /code/development/WebApplication


# Indica que se debe ejecutar el comando para correr la aplicación
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
