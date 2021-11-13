from django.contrib.auth.models import User
from django.db import models
import uuid

class Contact(models.Model):
    user = models.ForeignKey(User, related_name='friends', on_delete=models.CASCADE)
    friends = models.ManyToManyField('self', blank=True)
    

    def __str__(self):
        return self.user.username


class Room(models.Model):
    speakers = models.ManyToManyField(Contact, related_name='rooms', blank=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    room_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.id)


class Message(models.Model):
    contact = models.ForeignKey(Contact, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    chat = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.contact.user.username
