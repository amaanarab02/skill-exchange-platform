from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.user.username})"

class ExchangeRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_requests')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.sender} → {self.receiver} ({self.status})"
