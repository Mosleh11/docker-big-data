FROM python:3.9-slim

WORKDIR /app

# Installer Java (OpenJDK)
# On met à jour la liste des paquets et on installe le JRE par défaut
RUN apt-get update && \
    apt-get install -y default-jre && \
    rm -rf /var/lib/apt/lists/*

# Installer PySpark 
RUN pip install --no-cache-dir pyspark

# Copier le script
COPY app/main.py .

# Lancer le script
CMD ["python", "main.py"]