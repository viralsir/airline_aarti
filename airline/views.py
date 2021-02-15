from django.shortcuts import render,redirect
from .models import flight,passenger
# Create your views here.
def home(request):

    return render(request,"airline/home.html",{
        "flights":flight.objects.all()
    })

def flight_details(request,flight_id):
    flight_info=flight.objects.get(id=flight_id)
    return render(request,"airline/details.html",{
        "flight_info":flight_info,
        "Passenger_list":flight_info.passenger.all(),
        "Non_passenger_list":passenger.objects.exclude(flights=flight_info).all()
    })

def book(request,flight_id):
    if request.method == 'POST':
        flight_info=flight.objects.get(id=flight_id)
        passenger_info=passenger.objects.get(id=request.POST['passenger'])
        passenger_info.flights.add(flight_info)
        passenger_info.save()
        return redirect('home')
