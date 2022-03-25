from django.test import TestCase
from .models import Image,Category,Location
# Create your tests here.
class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name='Nature')

    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))
    
    #Test to save the method
    def test_save_method(self):
        self.category.save_cat()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)
    

class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(name="Africa")

    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    def test_save_method(self):
        self.location.save_loc()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

class ImageTestClass(TestCase):
    #setup mathod
    def setUp(self):
        self.image=Image(name='Desert',description='chalbi desert in Africa')

    #Test Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    #test to save method