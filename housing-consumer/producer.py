import json
from confluent_kafka import Producer

KAFKA_BROKER = "broker:29092"
KAFKA_TOPIC = "housing_topic"

producer_conf = {
    'bootstrap.servers': KAFKA_BROKER
}

producer = Producer(producer_conf)

def delivery_report(err, msg):
    if err:
        print("[producer] Échec de livraison:", err)
    else:
        print(f"[producer] Message livré sur {msg.topic()} partition {msg.partition()}")

message = {
    "longitude": -122.23,
    "latitude": 37.88,
    "housing_median_age": 52,
    "total_rooms": 880,
    "total_bedrooms": 129,
    "population": 322,
    "households": 126,
    "median_income": 8.3252,
    "median_house_value": 358500,
    "ocean_proximity": "NEAR BAY"
}

message_str = json.dumps(message)
producer.produce(KAFKA_TOPIC, message_str.encode('utf-8'), callback=delivery_report)
producer.flush()

print("[producer] Message envoyé.")