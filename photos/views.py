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
    photos = Image.find_by_location(locations)
    return render(request,'all-photos/location.html', {"photos":photos,"locations":locations,})

def photo(request,photo_id):
    try:
        photo = Image.objects.get(id=photo_id)
    except ValueError:
        raise Http404()

    return render(request,"all-photos/image.html",{"photo":photo})