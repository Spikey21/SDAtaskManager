from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Attachment(models.Model):
    name = models.CharField()
    file = models.FileField()


class Task(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField(blank=True)
    createDate = models.DateTimeField(auto_now_add=True)
    completeDate = models.DateTimeField(blank=True, null=True)
    importance = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.title} | {self.user}'

