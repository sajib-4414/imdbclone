from events.user_created import UserCreatedEvent
from app.db import User
import tortoise

async def handle_user_registered_event(data):
    event = UserCreatedEvent(**data)
    print("will create a same user now here..")
    print(f"username= {event.username}")
    print(f"email={event.username}")
    try:
        user = await User.create(username=event.username, email=event.email)
        print(f"user created on the Notification service with email {event.email}")
    except tortoise.exceptions.IntegrityError as e:
        print("Error creating user on the notification service. User with credentials exists already.")