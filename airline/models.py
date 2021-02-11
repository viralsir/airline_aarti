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


class passenger(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    flights=models.ManyToManyField(flight,related_name="passenger",blank=True)


    def __str__(self):
        return f"{self.first_name} - {self.last_name}"
