from email.mime import image
from unicodedata import name
from django.db import models

# Create your models here.
class Image(models.Model):
    
    name = models.CharField(max_length=35)
    description=models.CharField(max_length=200)

class Category(models.Model):
    name = models.CharField(max_length=35)

class Location(models.Model):
    name = models.CharField(max_length=35)
