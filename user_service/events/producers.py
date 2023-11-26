import json
from kafka import KafkaProducer
from events.topics import TOPIC_USER_REGISTERED
from events.user_created import UserCreatedEvent
try:
    producer = KafkaProducer(bootstrap_servers="kafka:29092")
except Exception as e:
    print(f"Error initializing Kafka producer: {e}")
    producer = None  # Set producer to None to indicate that it's not available
    
def send_kafka_event_user_created(username, email):
    if not producer:
        print("could not send event, producer not available...")
        return;
    
    data = {
        "username":username,
        "email":email
    }
    print("will now send kafka event.....reaady....")
    if UserCreatedEvent(**data).is_valid():
        print("sending kafka event.....")
        producer.send(TOPIC_USER_REGISTERED, json.dumps(data).encode("utf-8"))
        print(f"Done Sending...")