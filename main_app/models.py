from django.db import models
from django.contrib.auth.models import User


class Memory(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    center0 = models.FloatField()
    center1 = models.FloatField()
    zoom = models.FloatField()

    def __str__(self):
        return self.title
