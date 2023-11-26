import json
import time

from kafka import KafkaProducer
ORDER_KAFKA_TOPIC = "order_details"
# producer = KafkaProducer(bootstrap_servers="kafka:29092")
try:
    producer = KafkaProducer(bootstrap_servers="kafka:29092")
except Exception as e:
    print(f"Error initializing Kafka producer: {e}")
    producer = None  # Set producer to None to indicate that it's not available
    
def send_kafka_event(username, email):
    data = {
        "username":username,
        "email":email
    }
    
    producer.send(ORDER_KAFKA_TOPIC, json.dumps(data).encode("utf-8"))
    print(f"Done Sending...")
