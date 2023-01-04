from django.db import models
from django.contrib.auth.models import User


class Memory(models.Model):
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание', max_length=2000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)
    zoom = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Воспоминание'
        verbose_name_plural = 'Воспоминания'
