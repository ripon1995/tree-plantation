from django.db import models


class Customer(models.Model):
    profile_image = models.CharField(max_length=255)
