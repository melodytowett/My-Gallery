

from ast import Delete
from django.db import models



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name
    
    def save_cat(self):
        self.save()

    def delete_cat(self):
        self.delete()


class Location(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name

    def save_loc(self):
        self.save()
    def delete_loc(self):
        self.delete()

class Image(models.Model):
    name = models.CharField(max_length=35)
    description=models.CharField(max_length=200)
    my_image = models.ImageField(upload_to ='photos/', blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls,photo_id):
        images = cls.objects.filter(photo_id=photo_id)
        return images

    @classmethod
    def current_images(cls,location):
        images = cls.objects.filter(location__in=location)
        return images

    @classmethod
    def search_by_catgory(cls,search_term):
        photos = cls.objects.filter(category__name__icontains=search_term)
        return photos
       
    @classmethod
    def find_by_location(cls,search_by_location):
        photos = cls.objects.filter(location__name__icontains= search_by_location)
        return photos
