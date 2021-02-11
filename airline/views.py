from django.shortcuts import render
from .models import flight
# Create your views here.
def home(request):

    return render(request,"airline/home.html",{
        "flights":flight.objects.all()
    })

def flight_details(request,flight_id):
    return render(request,"airline/details.html",{
        "flight_info":flight.objects.get(id=flight_id)
    })