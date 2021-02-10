from django.shortcuts import render
from .models import flight
# Create your views here.
def home(request):

    return render(request,"airline/home.html",{
        "flights":flight.objects.all()
    })