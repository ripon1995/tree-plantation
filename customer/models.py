from django.db import models


class Customer(models.Model):
    profile_picture_link = models.CharField(max_length=255)
