from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Export(models.Model):
    STATUS_CHOICES = [
        ('queued', 'Queued'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='queued')
    task_id = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)  # Field for additional description or metadata....
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.user.username} - {self.file_name} - {self.get_status_display()}"