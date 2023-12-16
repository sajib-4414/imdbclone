import pickle
from kafka import KafkaProducer
from events.topics import TOPIC_USER_REGISTERED
from events.user_created import UserCreatedEvent

    
def send_kafka_event_user_created(username, email, role):
    
    data = {
        "username":username,
        "email":email,
        "role":role
    }
    if UserCreatedEvent(**data).is_valid():
        print("sending kafka event from user-service.....")
        try:
            producer = KafkaProducer(bootstrap_servers='kafka:9092') #there is an issue definining producer on top
            # it is not sending messages if defined on top and reuse it here.
            serialized_data = pickle.dumps(data, pickle.HIGHEST_PROTOCOL)
            print("data sent:")
            print(serialized_data)
            producer.send(TOPIC_USER_REGISTERED, serialized_data)
            print(f"Done Sending...")
           
        except Exception as e:
            print(f"Exception occurred: {e}")
            import traceback
            traceback.print_exc()
