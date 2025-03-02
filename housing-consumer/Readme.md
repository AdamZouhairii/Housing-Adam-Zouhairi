# Housing Consumer

## Description

Housing Consumer est un service Kafka qui écoute le topic `housing_topic`, consomme les messages en temps réel et les envoie à l’API FastAPI (`housing-api`). Ce service permet d'intégrer un flux de données en continu et d'automatiser le stockage des nouvelles données reçues.

---

## Prérequis

Avant d’exécuter ce service, assurez-vous d’avoir installé :

- **Docker** et **Docker Compose**
- **Python 3.12** (si vous souhaitez exécuter le consumer localement sans Docker)
- Un broker Kafka opérationnel (exécuté via `docker-compose` ou un cluster Kafka externe)

---

## Installation et Démarrage

### 1. Démarrer avec Docker

Si vous souhaitez exécuter le consumer avec Docker Compose, utilisez la commande suivante :

```bash
docker-compose up --build housing-consumer
```

Cela démarre :

- Le service Kafka Consumer (`housing-consumer`)

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

3. **Configurer les variables d'environnement** :

   Créez un fichier `.env` avec le contenu suivant :

   ```
   KAFKA_BROKER=broker:29092
   KAFKA_TOPIC=housing_topic
   API_ENDPOINT=http://housing_api:8000/houses
   ```

4. **Lancer le consumer** :

   ```bash
   python consumer.py
   ```

---

## Tester le Consumer

### 1. Vérifier la connexion au topic Kafka

```bash
docker-compose logs -f housing-consumer
```

Si tout fonctionne correctement, vous devriez voir le message :

```
[consumer] Démarrage du consumer, en attente des messages sur le topic 'housing_topic'...
```

### 2. Envoyer un message avec le Producer

Dans un autre terminal, exécutez :

```bash
docker-compose exec consumer python producer.py
```

Le producer va envoyer un message test au topic `housing_topic`.

### 3. Vérifier que le Consumer traite le message

Dans les logs du consumer (`docker-compose logs -f housing-consumer`), vous devriez voir :

```
[consumer] Message consommé et envoyé,
```

Cela signifie que le consumer a bien reçu un message depuis Kafka et l’a transmis à l’API.

---


## Développement et Debug

### Voir les logs en temps réel

```bash
docker-compose logs -f housing-consumer
```

### Entrer dans le container

```bash
docker exec -it housing_consumer /bin/sh
```

---

## Arrêter le service

Pour arrêter le service Kafka Consumer :

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

