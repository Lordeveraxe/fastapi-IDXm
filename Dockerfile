# Usa la imagen base de Python 3.8
FROM python:3.8

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requerimientos a la ubicación de trabajo en el contenedor
COPY requirements.txt /app/

# Configura el entorno virtual de Python
RUN python -m venv --copies /opt/venv
RUN . /opt/venv/bin/activate

# Actualiza pip a la última versión
RUN pip install --upgrade pip

# Instala las dependencias del proyecto desde requirements.txt
RUN pip install -r requirements.txt

# Copia el código de la aplicación al contenedor
COPY . /app/

# Comando para iniciar la aplicación FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "$PORT", "--reload"]