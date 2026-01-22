# Image de base légère
FROM python:3.9-slim

# On définit le dossier de travail
WORKDIR /app

# On copie d'abord les requirements pour le cache Docker
COPY app/requirements.txt .

# On installe pandas
RUN pip install --no-cache-dir -r requirements.txt

# On copie le script
COPY app/main.py .

# Commande par défaut : lancer le script
CMD ["python", "main.py"]