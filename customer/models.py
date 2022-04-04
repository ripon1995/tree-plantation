from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False, unique=True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
