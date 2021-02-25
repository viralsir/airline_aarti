from django.db import models
from django.urls import reverse
# ORM  : OBEJCT RELATIONAL MAPPING
# Create your models here.
class course_info(models.Model):
    #member variable
    name=models.CharField(max_length=30)
    descrition=models.TextField()
    duration=models.IntegerField()
    fees=models.IntegerField()

    #member function
    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return  reverse('view')