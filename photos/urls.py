from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
import photos
# app_name = 'photos'
urlpatterns = [
    path('',views.index, name='index'),
    path('search/',views.search_results,name='search_results'),
    path('location/',views.location_results, name = 'location_results'),
    path('<int:photo_id>/',views.photo,name='photo'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)