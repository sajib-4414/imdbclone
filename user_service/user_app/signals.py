from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from events.producers import send_kafka_event
@receiver(post_save, sender=User)
def on_user_registration(sender, instance, created, **kwargs):
    if created:
        print("usr created captured....")
        # This user is newly created, send Kafka event
        send_kafka_event(instance.username, instance.email)