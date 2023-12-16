from django.conf import settings
from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import AbstractUser

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        REGULAR_USER = "REGULAR_USER", "Regular_User"
        CONTENT_CREATOR_USER = "CONTENT_CREATOR_USER", "Content_Creator_User"

    base_role = Role.ADMIN
    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)
        