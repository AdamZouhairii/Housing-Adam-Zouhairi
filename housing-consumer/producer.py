import json
from confluent_kafka import Producer

KAFKA_BROKER = "localhost:29092"
producer = Producer({'bootstrap.servers': KAFKA_BROKER})

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

producer.produce('housing_topic', json.dumps(message).encode('utf-8'))
producer.flush()
print("Message envoyé")