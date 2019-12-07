from django.contrib import admin
from django.urls import path, include
from sightings import views

urlpatterns = [
    path('sightings/',include('sightings.urls')),
    path('admin/', admin.site.urls),
    path('map/',include('map.urls')),
    path('',views.home,name='home'),
]
