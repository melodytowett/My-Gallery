from email import message
from django.shortcuts import render

import photos
from.models import Image,Location
# Create your views here.
def index(request):
    location = Location.objects.all()
    photos = Image.current_images(location)
    return render(request,'index.html', {"photos":photos})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_name(search_term)
        message = "{search_term}"

        return render(request,'all-photos/search.html',{"message":message,"photos":searched_images})
    else:
        message = "You havent searched fro any term"
        return render(request,'all-photos/search.html',{"message":message})