import json
import os
import requests
from confluent_kafka import Consumer, KafkaException
from dotenv import load_dotenv

load_dotenv()

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:29092")
API_ENDPOINT = os.getenv("API_ENDPOINT", "http://housing_api:8000/houses")

consumer_conf = {
    'bootstrap.servers': KAFKA_BROKER,
    'group.id': 'housing_consumer_group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(consumer_conf)
consumer.subscribe(['housing_topic'])

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())
        # Décodage du message
        house_data = json.loads(msg.value().decode('utf-8'))
        # Envoi des données vers l'API
        response = requests.post(API_ENDPOINT, json=house_data)
        print("Message consommé et envoyé, réponse:", response.status_code, response.json())
except KeyboardInterrupt:
    pass
finally:
    consumer.close()