from unicodedata import category
from django.shortcuts import render

import photos
from.models import Category, Image,Location
# Create your views here.
def index(request):
    location = Location.objects.all()
    photos = Image.current_images(location)
    return render(request,'index.html', {"photos":photos})

def all(request):
    category = Category.objects.all()
    photos = Image.all_images(category)
    return render(request,'all-photos/category.html', {"category":category,"photos":photos})
    
def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_by_name(search_term)
        message = "{search_term}"

        return render(request,'all-photos/search.html',{"message":message,"category":searched_images})
    else:
        message = "You havent searched fro any term"
        return render(request,'all-photos/search.html',{"message":message})

def location_results(request):
    ''''''
    location = Location.objects.all()
    photos = Image.current_images(location)
    return render(request,'all-photos/location.html', {"photos":photos,"location":location})