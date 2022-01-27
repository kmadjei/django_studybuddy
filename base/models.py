# ?
from django.db import models
# ?
from django.contrib.auth.models import User

# Create your models here.

# each class represents a table in the django 
# variables are the columns/artributes of the table

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # makes the blog message display latest one at the top
        ordering = ['-updated', '-created']

    # __str__ -> returns the string representation of the object. This method is called when print() or str() function is invoked on an object
    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # makes the blog message display latest one at the top
        ordering = ['-updated', '-created']

    def __str__(self):
        # return first 50 characters of body string
        return self.body[0:50]