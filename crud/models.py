from django.db import models #type: ignore

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

