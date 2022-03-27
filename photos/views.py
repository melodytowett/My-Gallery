from email import message
from unicodedata import category
from django.http import Http404
from django.shortcuts import render

import photos
from.models import Category, Image,Location
# Create your views here.
def index(request):
    location = Location.objects.all()
    photos = Image.current_images(location)
    return render(request,'index.html', {"photos":photos})

def search_results(request):
    locations = Location.objects.all()

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_images = Image.search_by_catgory(search_term)
        message = f"{search_term}"
        return render(request,'all-photos/search.html',{"message":message, "locations":locations,"photos":searched_images})
    else:
        message = "You havent searched for any term"
        return render(request,'all-photos/search.html',{"message":message})

def location_results(request):
    ''''''
    locations = Location.objects.all()
    if 'phot'in request.GET and request.GET["photo"]:
        search_by_location = request.GET.get("photo")
        images_found = Image.find_by_location(search_by_location)
        message = f"{search_by_location}"
        return render(request,'all-photos/location.html', {"photos":images_found,"locations":locations,})
    else:
        message = "No images taken in that location"
        return render(request,'all-photos/location.html',{"message":message})

def photo(request,photo_id):
    try:
        photo = Image.objects.get(id=photo_id)
    except ValueError:
        raise Http404()

    return render(request,"all-photos/image.html",{"photo":photo})