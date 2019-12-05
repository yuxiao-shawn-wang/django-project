from django.shortcuts import render,HttpResponse, get_object_or_404,redirect
from .models import Squirrel
from .forms import SquirrelModelForm

# create a url function that can render the url to all.html, which can show all the sightings
def all_sightings(request):
    squirrels = Squirrel.objects.all()
    context = {'squirrels': squirrels}
    return render(request, 'sightings/all.html', context)

# create a detail funtion to check and update the detail information of a squirrel sighting
def squirrel_details(request,Unique_Squirrel_ID):
    squirrel = get_object_or_404(Squirrel, Unique_Squirrel_ID=Unique_Squirrel_ID)
    form = SquirrelModelForm(request.POST or None, instance = squirrel)
    context={
           'squirrel': squirrel,
           'form': form, }
    if request.method == 'POST':
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/sightings')

        else:
            return HttpResponse('Wrong!')
    
    else:
        form=SquirrelModelForm(instance=squirrel)
    return render(request, 'sightings/detail.html', context)


def delete(request, Unique_Squirrel_ID):
    squirrel = get_object_or_404(Squirrel, Unique_Squirrel_ID=Unique_Squirrel_ID)
    squirrel.delete()
    return HttpResponse('Successfully Delete it!')