from django.db import models

# Create your models here.

class Contact(models.Model):
    email = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)