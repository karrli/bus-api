from django.db import models

# Create your models here.

class Driver(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    owner = models.ForeignKey('auth.User', related_name='drivers', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    

class Schedule(models.Model):
    departure = models.DateTimeField(unique=True, null=True, blank=True)
    arrival = models.DateTimeField(unique=True, null=True, blank=True) 
    
class Route(models.Model):
    name = models.CharField(max_length=30)
    schedule = models.ManyToManyField(Schedule)
    owner = models.ForeignKey('auth.User', related_name='routes', on_delete=models.CASCADE)
    
class Bus(models.Model):
    driver = models.OneToOneField(
        Driver,
        on_delete=models.CASCADE,
    ) 
    route = models.ForeignKey(Route,on_delete=models.CASCADE) 
    plate = models.CharField(max_length=10)
    owner = models.ForeignKey('auth.User', related_name='buses', on_delete=models.CASCADE)
    

class Passenger(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bus = models.ForeignKey(Bus,on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='passengers', on_delete=models.CASCADE)

    #If new passenger, check route & bus capacity 
    #     @property
    # def sold_seats(self):
    #     if passenger.bus.count()<10
    #     return self.passenger_set
    #     else 

