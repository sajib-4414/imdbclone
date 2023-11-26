from events.user_created import UserCreatedEvent
def handle_user_registered_event(data):
    event = UserCreatedEvent(**data)
    print("successfully received user created event..., will create user now.")
    print(f"username= {event.username}")
    print(f"email={event.username}")