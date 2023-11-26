import django.db
from events.user_created import UserCreatedEvent
from django.contrib.auth.models import User

def handle_user_registered_event(data):
    event = UserCreatedEvent(**data)
    print("successfully received user created event in Movie service..., will create user now.")
    print(f"username= {event.username}")
    print(f"email={event.username}")
    try:
        user = User.objects.create(username=event.username, email=event.email)
        print(f"user created on the Movie service with email {event.email}")
    except django.db.IntegrityError as e:
        print(f"Error creating user on the movie service, user with credentials exists already")
        
    