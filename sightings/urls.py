from django.urls import path
from . import views


app_name = 'sightings'
urlpatterns = [
    # add an url path that can view all the sightings
    path('', views.all_sightings, name='list'),
    # add an url path that can view the stats about Squirrel Data
    path('stats', views.stats, name='stats'),
    # add an url path than can view and update  the ditail of a specific sighting
    path('<Unique_Squirrel_ID>', views.squirrel_details, name='detail'),
    path('<Unique_Squirrel_ID>/update', views.squirrel_details, name = 'update'),
    # add the url path to delete the sighting
    path('<Unique_Squirrel_ID>/delete', views.delete, name='delete'),
    ]

