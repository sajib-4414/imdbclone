# kafka_consumer.py
from aiokafka import AIOKafkaConsumer
import pickle
from app.topics import TOPIC_USER_REGISTERED
from events.listeners import handle_user_registered_event
async def kafka_consumer():
    print("Listening to Kafka... On Notification service...")
    topics_all = [TOPIC_USER_REGISTERED]

    consumer = AIOKafkaConsumer(
        *topics_all,
        bootstrap_servers='kafka:9092',
        group_id="notification_group")
    # Get cluster layout and join group `my-group`
    await consumer.start()

    try:
        # Consume messages
        async for message in consumer:
            await process_kafka_event(message)
            # print("consumed: ", msg.topic, msg.partition, msg.offset,
            #       msg.key, msg.value, msg.timestamp)
    except Exception as e:
    # Handle the error and print a generic message
        print(f"An error occurred during reading kafka message on the notificaiton consumer: {e}")

    finally:
        pass
        # Will leave consumer group; perform autocommit if enabled.
        # await consumer.stop()


async def process_kafka_event(message):
    topic = message.topic
    deserialized_data = pickle.loads(message.value)
    print("message received on the notification service") 
    print(deserialized_data)
    if topic == TOPIC_USER_REGISTERED:
        await handle_user_registered_event(deserialized_data)
