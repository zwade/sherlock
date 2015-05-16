from django.db import models
from django.contrib.auth.models import User


class Hunt(models.Model):
    owner = models.ForeignKey(User, related_name="hunts")
    participants = models.ManyToManyField(User)
    description = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    photo = models.ImageField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
