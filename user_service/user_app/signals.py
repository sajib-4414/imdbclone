from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
User = get_user_model()
from user_app.models import ContentCreatorUser,RegularUser, ContentCreatorProfile, RegularUserProfile

from events.producers import send_kafka_event_user_created
@receiver(post_save, sender=ContentCreatorUser)
def on_creator_user_registration(sender, instance, created, **kwargs):
    if created:
        print("creator user created captured....")
        # This user is newly created, send Kafka event
        send_kafka_event_user_created(instance.username, instance.email, str(instance.role))
        
@receiver(post_save, sender=RegularUser)
def on_regular_user_registration(sender, instance, created, **kwargs):
    if created:
        print("regular user created captured....")
        # This user is newly created, send Kafka event
        send_kafka_event_user_created(instance.username, instance.email, str(instance.role))

@receiver(post_save, sender=ContentCreatorUser)
def create_content_creator_profile(sender, instance, created, **kwargs):
    if created and instance.role == "CONTENT_CREATOR_USER":
        ContentCreatorProfile.objects.create(user=instance)   

@receiver(post_save, sender=RegularUser)
def create_regular_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "REGULAR_USER":
        RegularUserProfile.objects.create(user=instance)  