from django.http import HttpResponse
from django.shortcuts import render
from . models import Place, Person

# Create your views here.
def demo(request):
    obj = Place.objects.all()
    person = Person.objects.all()
    return render(request, "index.html", {'obj': obj, 'obj1': person})


