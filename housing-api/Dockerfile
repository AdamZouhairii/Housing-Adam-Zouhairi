FROM python:3.12

# Installer les dépendances système
RUN apt-get update && apt-get install -y gcc libpq-dev

WORKDIR /app

# Copier les fichiers de configuration
COPY pyproject.toml poetry.lock* ./

# Installer Poetry
RUN pip install poetry && poetry config virtualenvs.create false

# Installer les dépendances Python
RUN poetry install --no-root

# Copier le reste du code
COPY . .

# Copier le script wait-for-it et le rendre exécutable
COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

# Exposer le port de l'API
EXPOSE 8000

# La commande de démarrage est définie dans docker-compose.yml
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]