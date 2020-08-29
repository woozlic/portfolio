from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    text = models.TextField()