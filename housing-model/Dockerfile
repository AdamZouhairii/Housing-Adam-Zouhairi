FROM python:3.12

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y gcc

WORKDIR /app

# Copier les fichiers de configuration Poetry
COPY pyproject.toml poetry.lock* ./

# Installer Poetry et configurer pour installer dans l'environnement système
RUN pip install poetry && poetry config virtualenvs.create false

# Installer les dépendances Python
RUN poetry install --no-root

# Copier le reste du code du projet
COPY . .

# Exposer le port de l'API d'inférence (8002)
EXPOSE 8002

# Lancer l'application FastAPI avec Uvicorn sur le port 8002
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8002"]