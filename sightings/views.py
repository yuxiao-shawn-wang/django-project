from django.shortcuts import render,HttpResponse, get_object_or_404
from .models import Squirrel

# create a url function that can render the url to all.html, which can show all the sightings
def all_sightings(request):
    squirrels = Squirrel.objects.all()
    context = {'squirrels': squirrels}
    return render(request, 'sightings/all.html', context)


def squirrel_details(request,Unique_Squirrel_ID):
    squirrel = get_object_or_404(Squirrel, Unique_Squirrel_ID=Unique_Squirrel_ID)
    context={'squirrel': squirrel}
    return render(request, 'sightings/detail.html', context)
