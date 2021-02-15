from django.urls import path
from . import  views
urlpatterns=[
    path("home",views.home,name="home"),
    path("detail/<int:flight_id>",views.flight_details,name="flight_details"),
    path("book/<int:flight_id>",views.book,name="book")
]