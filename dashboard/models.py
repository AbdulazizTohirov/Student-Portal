from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Notes Model
class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title  = models.CharField(max_length=255)
    description = models.TextField()
    
    class Meta:
        verbose_name = 'notes'
        verbose_name_plural = 'notes'

    def __str__(self):
        return self.title


# Homework Model
class Homework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due = models.DateTimeField()
    is_finished = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title


# To Do Model
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title