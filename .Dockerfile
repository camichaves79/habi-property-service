# Usa una imagen base de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /usr/src/app

# Copia los archivos de requirements y el código fuente
COPY requirements.txt ./
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que la API correrá
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
