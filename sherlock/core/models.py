from django.db import models
from django.contrib.auth.models import User
import random
import string


def random_string(N):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(N))


class Hunt(models.Model):
    owner = models.ForeignKey(User, related_name="hunts")
    participants = models.ManyToManyField(User, blank=True)
    description = models.TextField(max_length=1000)
    name = models.CharField(max_length=100)
    photo = models.ImageField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    slug = models.CharField(max_length=8, unique=True, blank=True)

    def save(self):
        if not self.slug:
            self.slug = random_string(8)
        super(Hunt, self).save()

    def __str__(self):
        return self.name


class Clue(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField(max_length=500, blank=True)
    points = models.IntegerField()

    hunt = models.ForeignKey(Hunt)

    def __str__(self):
        return "{} (Hunt '{}')".format(self.name, self.hunt.name)


class Submission(models.Model):
    image = models.ImageField(upload_to='submissions')
    time = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=200)

    valid = models.BooleanField()
    verified = models.BooleanField()

    clue = models.ForeignKey(Clue)
    user = models.ForeignKey(User)

    def __str__(self):
        return "User '{}' to Clue '{}')".format(self.user, self.clue)
