import json
import time
import socket
import requests
from confluent_kafka import Consumer, KafkaException

# On force ici l'utilisation du broker interne
KAFKA_BROKER = "broker:29092"
API_ENDPOINT = "http://housing_api:8000/houses"
KAFKA_TOPIC = "housing_topic"

def wait_for_broker(broker, timeout=60):
    host, port_str = broker.split(':')
    port = int(port_str)
    start = time.time()
    while time.time() - start < timeout:
        try:
            # Tente de se connecter au broker
            with socket.create_connection((host, port), timeout=5) as sock:
                print(f"[wait_for_broker] Broker {broker} est disponible.")
                return
        except Exception as e:
            # Affiche un message d'attente si la connexion échoue
            print(f"[wait_for_broker] En attente de {broker}... ({e})")
            time.sleep(2)
    # Lève une exception si le broker n'est pas disponible après le délai imparti
    raise Exception(f"Broker {broker} non disponible après {timeout} secondes.")

# Attendre que le broker Kafka soit joignable
wait_for_broker(KAFKA_BROKER)

# Configuration du consumer Kafka
consumer_conf = {
    'bootstrap.servers': KAFKA_BROKER,
    'group.id': 'housing_consumer_group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(consumer_conf)
consumer.subscribe([KAFKA_TOPIC])

# Indique que le consumer est démarré et en attente de messages
print(f"[consumer] Démarrage du consumer, en attente des messages sur le topic '{KAFKA_TOPIC}'...")

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        # Affiche une erreur si la lecture du message échoue
        print("[consumer] Erreur lors de la lecture du message:", msg.error())
        continue
    try:
        # Tente de traiter le message reçu
        data = json.loads(msg.value().decode('utf-8'))
        response = requests.post(API_ENDPOINT, json=data)
        # Affiche le statut de la réponse après envoi du message
        print("[consumer] Message consommé et envoyé, réponse:", response.status_code, response.json())
    except Exception as e:
        # Affiche une erreur si le traitement du message échoue
        print("[consumer] Erreur lors du traitement du message:", e)

# Ferme le consumer proprement
consumer.close()