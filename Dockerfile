# Dockerfile (unificado)
FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl unzip build-essential git && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install --upgrade reflex

COPY . .

EXPOSE 8000 3000

CMD ["reflex", "run", "--backend-host", "0.0.0.0"]
