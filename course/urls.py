from django.urls import path
from . import views

urlpatterns=[
    path("new",views.NewCourse.as_view(),name="insert")
]