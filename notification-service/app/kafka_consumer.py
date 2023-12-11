# kafka_consumer.py
from kafka import KafkaConsumer
import pickle
from app.topics import TOPIC_USER_REGISTERED
def kafka_consumer():
    print("listening to kafka events on the notification service")
    topics_all = [TOPIC_USER_REGISTERED]
    consumer = KafkaConsumer(*topics_all, 
        bootstrap_servers=['kafka:9092'], 
        api_version=(0, 10) 
        #,consumer_timeout_ms=1000
        )

    for message in consumer:
        process_kafka_event(message)

def process_kafka_event(message):
    topic = message.topic
    deserialized_data = pickle.loads(message.value)
    print("message received on the notification service") 
    print(deserialized_data)
    # if topic == TOPIC_USER_REGISTERED:
    #     handle_user_registered_event(deserialized_data)
