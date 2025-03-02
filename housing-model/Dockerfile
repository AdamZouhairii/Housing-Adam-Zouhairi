FROM python:3.12

# Met à jour les paquets et installe gcc
RUN apt-get update && apt-get install -y gcc

WORKDIR /app

# Copie les fichiers de configuration de Poetry
COPY pyproject.toml poetry.lock* ./

# Installe Poetry et configure pour installer dans l'environnement système
RUN pip install poetry && poetry config virtualenvs.create false

# Installe les dépendances Python
RUN poetry install --no-root

# Copie le reste du code du projet
COPY . .

# Expose le port de l'API d'inférence (8002)
EXPOSE 8002

# Lance l'application FastAPI avec Uvicorn sur le port 8002
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8002"]