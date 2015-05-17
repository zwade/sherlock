from django.db import models
from django.contrib.auth.models import User
import random
import string
from django.utils import timezone as datetime


def random_string(N):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(N))


class Hunt(models.Model):
    owner = models.ForeignKey(User, related_name='owned_hunts')
    participants = models.ManyToManyField(User, blank=True, related_name='joined_hunts')
    description = models.TextField(max_length=1000)
    name = models.CharField(max_length=100)
    photo = models.ImageField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    slug = models.SlugField(max_length=8, unique=True, blank=True)

    def save(self):
        if not self.slug:
            self.slug = random_string(8)
        super(Hunt, self).save()

    def started(self):
        return datetime.now() > self.start_time

    def active(self):
        return self.start_time < datetime.now() < self.end_time

    def __str__(self):
        return self.name


class Clue(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField(max_length=500, blank=True)
    points = models.IntegerField()

    hunt = models.ForeignKey(Hunt, related_name='clues')

    def __str__(self):
        return "Clue '{}' of Hunt '{}'".format(self.name, self.hunt.name)


class Submission(models.Model):
    image = models.ImageField(upload_to='submissions')
    time = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=200)

    valid = models.BooleanField(default=True)
    verified = models.BooleanField(default=False)

    clue = models.ForeignKey(Clue, related_name='submissions')
    user = models.ForeignKey(User, related_name='submissions')

    def __str__(self):
        return "Submission by User '{}' to '{}'".format(self.user, self.clue)
