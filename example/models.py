from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    #username = models.CharField(max_length=200, unique=True, null=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class UserSchedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        unique_together = ("user", "date", "time")

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200) #length is required
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True) #takes a time stamp every single time it was updated
    created = models.DateTimeField(auto_now_add=True) #only takes a time stamp when we save or create a group
    schedules = models.ManyToManyField(UserSchedule, blank=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name #has to be a stirng 


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #first relationship a mini two one relationship, one model ot many children
    room = models.ForeignKey(Room, on_delete=models.CASCADE) #deletes all the messages/ possibly data in a room
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]
    