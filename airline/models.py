from django.db import models
# Create your models here.
class airport(models.Model):
    city=models.CharField(max_length=40)
    code=models.CharField(max_length=40)

    def __str__(self):
        return f"Airport({self.city})"


class flight(models.Model):
    origin=models.ForeignKey(airport,on_delete=models.CASCADE,related_name='departure')
    destination=models.ForeignKey(airport,on_delete=models.CASCADE,related_name='arrival')
    duration=models.IntegerField()

    def __str__(self):
        return f"flight({self.origin} to {self.destination})"
