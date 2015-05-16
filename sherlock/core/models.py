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


class Clue(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField(max_length=500)
    points = models.IntegerField()

    hunt = models.ForeignKey(Hunt)


class Submission(models.Model):
    image = models.ImageField(upload_to='submissions')
    time = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=200)

    valid = models.BooleanField()
    verified = models.BooleanField()

    clue = models.ForeignKey(Clue)
    user = models.ForeignKey(User)
