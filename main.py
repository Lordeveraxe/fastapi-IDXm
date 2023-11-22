from fastapi import FastAPI, File, UploadFile
import requests
from tensorflow.keras.models import load_model
from io import BytesIO
from PIL import Image
import numpy as np

app = FastAPI()

# URL del modelo
model_url = "https://drive.google.com/uc?id=1wMb03-UkWY2PmWkvZKUxXZppuINfOFza"

# Descargar el modelo
response = requests.get(model_url)
model_file = BytesIO(response.content)

# Cargar el modelo
model = load_model(model_file)

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Convertir el archivo cargado en una imagen
    image = Image.open(BytesIO(await file.read()))
    image = image.resize((224, 224)) # Asegúrate de cambiar el tamaño según tu modelo
    image = np.expand_dims(image, axis=0)

    # Realizar predicción
    prediction = model.predict(image)

    return {"prediction": prediction.tolist()}