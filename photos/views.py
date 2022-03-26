from django.shortcuts import render

import photos
from.models import Image,Location
# Create your views here.
def index(request):
    location = Location.objects.all()
    photos = Image.current_images(location)
    return render(request,'index.html', {"photos":photos})