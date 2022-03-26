
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
    name = models.CharField(max_length=35)
    description=models.CharField(max_length=200)
    my_image = models.ImageField(upload_to ='', blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def all_images(cls,category):
        images = cls.objects.filter(category__in=category)
        return images

    @classmethod
    def current_images(cls,location):
        images = cls.objects.filter(location__in=location)
        return images

    @classmethod
    def search_by_name(cls,search_term):
        images = cls.objects.filter(category_name__icontains=search_term)
        return images
    # @classmethod
    # def display_by_category(cls,category)