from events.user_created import UserCreatedEvent
from app.db import database, User

async def handle_user_registered_event(data):
    event = UserCreatedEvent(**data)
    print("successfully received user created event in Movie service..., will create user now.")
    print(f"username= {event.username}")
    print(f"email={event.username}")
    try:
        user = await User.objects.create(username=event.username, email=event.email)
        print(f"user created on the Notification service with email {event.email}")
    except django.db.IntegrityError as e:
        print(f"Error creating user on the movie service, user with credentials exists already")