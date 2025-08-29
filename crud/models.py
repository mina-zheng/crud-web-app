from django.db import models #type: ignore
from django.contrib.postgres.fields import ArrayField #type: ignore

class Users(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    liked_book_indices = models.CharField()

class Books(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()


