from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
User = get_user_model()

from events.producers import send_kafka_event_user_created
@receiver(post_save, sender=User)
def on_user_registration(sender, instance, created, **kwargs):
    if created:
        print("user created captured....")
        print("user role=",str(instance.role))
        t =type(instance.role)
        print("type=",t)
        # This user is newly created, send Kafka event
        send_kafka_event_user_created(instance.username, instance.email, str(instance.role))