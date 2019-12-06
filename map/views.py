from django.shortcuts import render
from sightings.models import Squirrel
# Create your views here.
def show_map(request):
	squirrels = Squirrel.objects.all()
	context = {'squirrels': squirrels}
	return render(request, 'map/show_map.html', context)
# Create your views here.
