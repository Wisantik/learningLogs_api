from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=200, blank=True)
    user = models.ForeignKey(
        User, verbose_name="пользователь", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Entrys(models.Model):
    content = models.TextField()
    topic = models.ForeignKey("Topic", on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, verbose_name="пользователь", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.content[:55]
