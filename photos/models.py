
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name
    
    def save_cat(self):
        self.save()


class Location(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name

    def save_loc(self):
        self.save()

class Image(models.Model):
    image = models.ImageField(upload_to ='photos/', blank=True)
    name = models.CharField(max_length=35)
    description=models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()