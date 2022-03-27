
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

    def test_delete_category(self):
        self.category.save_cat()
        self.category.delete_cat()
        self.assertTrue(len(Category.objects.all())==0)

    # def test_update_category(self):
    #     update_cat = Category.update_category('Travel','Food')
    #     self.assertEqual(update_cat.name,'Travel')

    

class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(name="Africa")

    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    def test_save_method(self):
        self.location.save_loc()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)
    def test_delete_location(self):
        self.location.save_loc()
        self.location.delete_loc()
        self.assertTrue(len(Location.objects.all())==0)

class ImageTestClass(TestCase):
    #setup mathod
    def setUp(self):
        self.image=Image(name='Desert',description='chalbi desert in Africa')
        self.image.save_image()
    #Test Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))
        
    #test to save method

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    # def test_get_images_by_location(self):
    #     current_image = Image.current_images(location=)
    #     self.assertTrue(len(current_image)>0)