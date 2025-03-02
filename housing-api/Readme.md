# Housing API

## Description

Housing API est un service RESTful basé sur FastAPI permettant de gérer une base de données de logements.
Il permet d'ajouter de nouveaux logements et de récupérer la liste des logements stockés dans une base de données PostgreSQL.

---

## Prérequis

Avant d’exécuter ce service, assurez-vous d’avoir installé :

- **Docker** et **Docker Compose**
- **Python 3.12** (si vous souhaitez exécuter l'API localement sans Docker)

---

## Installation et Démarrage

### 1. Démarrer avec Docker

Si vous souhaitez exécuter l'API avec Docker Compose, utilisez la commande suivante :

```bash
docker-compose up --build housing-api
```

Cela démarre :

- Le service FastAPI (housing-api)
- La base de données PostgreSQL (si elle est définie dans `docker-compose.yml`)

L'API sera accessible à l'adresse suivante :

```
http://localhost:8000
```

### 2. Démarrer localement sans Docker

Si vous souhaitez exécuter l’API sans Docker, suivez ces étapes :

1. **Créer un environnement virtuel** (optionnel mais recommandé) :

   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur macOS/Linux
   venv\Scripts\activate     # Sur Windows
   ```

2. **Installer les dépendances** :

   ```bash
   pip install -r requirements.txt
   ```

3. **Démarrer un serveur PostgreSQL localement** et configurer les variables d’environnement dans un fichier `.env` :

   ```
   DB_USER=postgres
   DB_PASSWORD=postgres
   DB_NAME=housing_db
   DB_HOST=localhost
   DB_PORT=5432
   ```

4. **Appliquer les migrations** :

   ```bash
   alembic upgrade head
   ```

5. **Lancer l’API** :

   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

---

## Tester l'API

### 1. Vérifier que l'API est accessible

Dans un terminal, exécutez :

```bash
curl http://localhost:8000/houses
```

Si aucun logement n’a encore été ajouté, la réponse sera `[]`.

### 2. Ajouter un logement (POST /houses)

```bash
curl -X POST -H "Content-Type: application/json" -d '{
  "longitude": -122.23,
  "latitude": 37.88,
  "housing_median_age": 41,
  "total_rooms": 880,
  "total_bedrooms": 129,
  "population": 322,
  "households": 126,
  "median_income": 8.3252,
  "median_house_value": 452600.0,
  "ocean_proximity": "NEAR BAY"
}' http://localhost:8000/houses
```

### 3. Vérifier que les données ont bien été enregistrées

```bash
curl http://localhost:8000/houses
```

---


---

## Développement et Debug

### Voir les logs en temps réel

```bash
docker-compose logs -f housing-api
```

### Entrer dans le container

```bash
docker exec -it housing_api /bin/sh
```

### Appliquer les migrations manuellement

```bash
docker-compose exec housing-api alembic upgrade head
```

---

## Arrêter l'API

Pour arrêter l'API et tous les services liés :

```bash
docker-compose down
```

Pour tout supprimer (conteneurs, volumes, réseaux) :

```bash
docker-compose down -v
```

---

## Licence

Ce projet est sous licence MIT. Vous pouvez le modifier et l’utiliser librement.

---
