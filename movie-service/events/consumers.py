from events.topics import TOPIC_USER_REGISTERED
from events.event_listeners import handle_user_registered_event
from kafka import KafkaConsumer
import pickle

def start_consumer():
    print("listening to kafka events....")
    topics = [TOPIC_USER_REGISTERED]
    consumer = KafkaConsumer(*topics, 
    bootstrap_servers=['kafka:9092'], 
    api_version=(0, 10) 
    #,consumer_timeout_ms=1000
    )

    for message in consumer:
        topic = message.topic
        deserialized_data = pickle.loads(message.value)
        print("message received on the movie service") 
        print(deserialized_data)
        if topic == TOPIC_USER_REGISTERED:
            handle_user_registered_event(deserialized_data)