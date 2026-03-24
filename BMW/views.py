from django.shortcuts import render
from .models import Car, Owner
from django.http import HttpResponse

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})

def owner_list(request):
    owners = Owner.objects.all()
    output = ', '.join([owner.name for owner in owners])
    return HttpResponse("Owner list: " + output)        

# Create your views here.
