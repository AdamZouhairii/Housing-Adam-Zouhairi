# Housing Model

## Description

Housing Model est un service de machine learning qui prédit la valeur médiane d’un logement en fonction de ses caractéristiques. Il est basé sur un modèle entraîné avec les données du marché immobilier de Californie.

---

## Prérequis

Avant d’exécuter ce service, assurez-vous d’avoir installé :

- **Docker** et **Docker Compose**
- **Python 3.12** (si vous souhaitez exécuter le modèle localement sans Docker)
- **MLflow** pour la gestion des expérimentations
- **Kaggle API** pour télécharger le dataset

---

## Installation et Démarrage

### 1. Démarrer avec Docker

Si vous souhaitez exécuter le modèle avec Docker Compose, utilisez la commande suivante :

```bash
docker-compose up --build housing-model
```

Cela démarre :

- Le service d’inférence du modèle ML

L'API sera accessible à l'adresse suivante :

```
http://localhost:8002
```

### 2. Démarrer localement sans Docker

1. **Créer un environnement virtuel** :

   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur macOS/Linux
   venv\Scripts\activate     # Sur Windows
   ```

2. **Installer les dépendances** :

   ```bash
   pip install -r requirements.txt
   ```

3. **Télécharger le dataset (optionnel)** :

   ```bash
   kaggle datasets download -d camnugent/california-housing-prices
   unzip california-housing-prices.zip -d data/
   ```

4. **Entraîner le modèle** :

   ```bash
   python train.py
   ```

5. **Lancer l’API d’inférence** :

   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8002
   ```

---

## Tester l'API du modèle

### 1. Vérifier que l'API est accessible

```bash
curl http://localhost:8002
```

Vous devriez obtenir une réponse indiquant que le serveur est en fonctionnement.

### 2. Faire une prédiction (POST /predict)

```bash
curl -X POST -H "Content-Type: application/json" -d '{
  "longitude": -122.23,
  "latitude": 37.88,
  "housing_median_age": 41,
  "total_rooms": 880,
  "total_bedrooms": 129,
  "population": 322,
  "households": 126,
  "median_income": 8.3252
}' http://localhost:8002/predict
```

La réponse ressemblera à :

```json
{
  "predicted_median_house_value": 356700
}
```

---


## Développement et Debug

### Voir les logs en temps réel

```bash
docker-compose logs -f housing-model
```

### Entrer dans le container

```bash
docker exec -it housing_model /bin/sh
```

---

## Arrêter le service

Pour arrêter le service du modèle ML :

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
