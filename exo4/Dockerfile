FROM python:3.8-slim-bullseye

WORKDIR /app

# Installation de Java
RUN apt-get update && \
    apt-get install -y default-jre && \
    rm -rf /var/lib/apt/lists/*


RUN pip install --no-cache-dir pyspark==3.3.0

COPY app/main.py .

CMD ["python", "main.py"]