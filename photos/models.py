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

    @classmethod
    def current_images(cls,location):
        images = cls.objects.filter(location__in=location)
        return images
