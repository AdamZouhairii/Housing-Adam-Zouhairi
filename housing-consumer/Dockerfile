FROM python:3.12

WORKDIR /app

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y gcc libpq-dev

# Copier le fichier de configuration Poetry et installer les dépendances Python
COPY pyproject.toml poetry.lock* ./
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-root

# Copier les scripts consumer.py et producer.py
COPY consumer.py /app/consumer.py
COPY producer.py /app/producer.py

# Lancer le consumer directement
CMD ["python", "consumer.py"]