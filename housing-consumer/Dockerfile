FROM python:3.12

WORKDIR /app

# Met à jour la liste des paquets et installe les dépendances système nécessaires
RUN apt-get update && apt-get install -y gcc libpq-dev

# Copie le fichier de configuration Poetry et installe les dépendances Python
COPY pyproject.toml poetry.lock* ./
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-root

# Copie les scripts consumer.py et producer.py
COPY consumer.py /app/consumer.py
COPY producer.py /app/producer.py

# Lance le consumer directement
CMD ["python", "consumer.py"]