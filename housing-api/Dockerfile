FROM python:3.12

# Met à jour les paquets et installe les dépendances système nécessaires
RUN apt-get update && apt-get install -y gcc libpq-dev

WORKDIR /app

# Copie les fichiers de configuration nécessaires pour Poetry
COPY pyproject.toml poetry.lock* ./

# Installe Poetry et configure pour ne pas créer d'environnements virtuels
RUN pip install poetry && poetry config virtualenvs.create false

# Installe les dépendances Python définies dans pyproject.toml
RUN poetry install --no-root

# Copie le reste du code de l'application dans le conteneur
COPY . .

# Copie le script wait-for-it et le rend exécutable
COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

# Expose le port 8000 pour accéder à l'API
EXPOSE 8000

# Définit la commande de démarrage de l'application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]