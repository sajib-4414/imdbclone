from django.conf import settings
from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.dispatch import receiver

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
        super().save(*args, **kwargs)
class ContentCreatorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    creator_verification_id = models.IntegerField(null=True, blank=True)

class ContentCreatorManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CONTENT_CREATOR_USER)

# It is a proxy model, creates the User isntance actually in the database
class ContentCreatorUser(User):
    base_role = User.Role.CONTENT_CREATOR_USER
    objects = ContentCreatorManager()  # this is needed as it filters out students,
    # now Student.objects.all() returns all users, but Student.student.all() returns all studeents only

    class Meta:
        proxy = True

    def welcome(self):
        return "only content creators are allowed to"
    

class RegularUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_verification_id = models.IntegerField(null=True, blank=True)

class RegularUserManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.REGULAR_USER)

# It is a proxy model, creates the User isntance actually in the database
class RegularUser(User):
    base_role = User.Role.REGULAR_USER
    objects = RegularUserManager()  # this is needed as it filters out students,
    # now Student.objects.all() returns all users, but Student.student.all() returns all studeents only

    class Meta:
        proxy = True

    def welcome(self):
        return "only regular users are allowed to"
    

           
# a dummy class to create permissions only.        
class ProContentCreatorPermissions(models.Model):
            
    class Meta:
        managed = False
        default_permissions = () # disable "add", "change", "delete"
                                 # and "view" default permissions

        permissions = ( 
            ('create_content', 'Create Content'),  
            ('update_content', 'Update the contents'), 
            ('delete_content', 'Delete the contents'), 
            ('read_content', 'Read all the contents'), 
        )