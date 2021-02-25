from django.urls import path
from . import views

urlpatterns=[
    path("new",views.NewCourse.as_view(),name="insert"),
    path("view",views.ListCourse.as_view(),name="view"),
    path("update/<int:pk>",views.UpdateCourse.as_view(),name="update")
]