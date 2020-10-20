from django.db import models
from datetime import date

# Create your models here.
from django.utils import timezone


class Todo(models.Model):
    content = models.CharField(max_length=255)
    isDone = models.BooleanField(default=False)

class Exercise(models.Model):
    today = models.DateTimeField(default=timezone.now)
    nickname = models.CharField(max_length=100, default='0')
    exer_title = models.CharField(max_length=100)
    exer_time = models.IntegerField()
    exer_date = models.DateField(max_length=100, default=timezone.now)


