from django.db import models
from django.contrib.auth.models import User


class Memory(models.Model):
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание', max_length=2000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    center0 = models.FloatField(default=6747055)
    center1 = models.FloatField(default=7729412)
    zoom = models.FloatField(default=10)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Воспоминание'
        verbose_name_plural = 'Воспоминания'
