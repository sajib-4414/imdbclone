from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
User = get_user_model()
from user_app.models import ContentCreatorUser, ContentCreatorProfile

from events.producers import send_kafka_event_user_created
@receiver(post_save, sender=User)
def on_user_registration(sender, instance, created, **kwargs):
    if created:
        print("user created captured....")
        # This user is newly created, send Kafka event
        send_kafka_event_user_created(instance.username, instance.email, str(instance.role))

@receiver(post_save, sender=ContentCreatorUser)
def create_content_creator_profile(sender, instance, created, **kwargs):
    if created and instance.role == "CONTENT_CREATOR_USER":
        ContentCreatorProfile.objects.create(user=instance)   