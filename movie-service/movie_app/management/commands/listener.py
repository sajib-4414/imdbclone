from django.core.management.base import BaseCommand
from kafka import KafkaConsumer
import pickle

class Command(BaseCommand):
    help = 'Listen to Kafka events'
    
    def handle(self, *args, **options):
        print("listening to kafka events....")
        consumer = KafkaConsumer('Ptopic', 
        bootstrap_servers=['kafka:9092'], 
        api_version=(0, 10) 
        #,consumer_timeout_ms=1000
        )

        for message in consumer:
            deserialized_data = pickle.loads(message.value)
            print("message received on the movie service") 
            print(deserialized_data)
        # ORDER_KAFKA_TOPIC = "Ptopic"
        # consumer = KafkaConsumer(
        # ORDER_KAFKA_TOPIC,
        # bootstrap_servers="kafka:29092"
        # )

        # try:
        #     for message in consumer:
        #         print(f"Received message: {message.value}")
        # except KeyboardInterrupt:
        #     pass
        # finally:
        #     consumer.close()

# def listen_to_kafka():
#     ORDER_KAFKA_TOPIC = "order_details"
#     consumer = KafkaConsumer(
#     ORDER_KAFKA_TOPIC,
#     bootstrap_servers="kafka:29092"
#     )

#     for message in consumer:
#         print(f"Received message: {message.value}")

# if __name__ == "__main__":
#     listen_to_kafka()