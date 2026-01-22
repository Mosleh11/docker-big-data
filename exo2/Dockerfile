FROM python:3.9-slim

WORKDIR /app

# Installation de Jupyter et des libs de Data Science
RUN pip install --no-cache-dir jupyterlab pandas matplotlib seaborn

# On expose le port 8888 (standard pour Jupyter)
EXPOSE 8888

# Commande pour lancer Jupyter
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]