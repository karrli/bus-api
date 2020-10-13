from rest_framework import serializers
from django.contrib.auth.models import User
from buses.models import Bus, Driver, Route, Passenger, Schedule

class DriverSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Driver
        fields = [
        'id',    
        'name',
        'last_name',
        'owner'    
        ]

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = [
        'id',
        'departure',
        'arrival'
        ]

class RouteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Route
        fields = [
        'id',
        'name',
        'schedule',
        'owner'
        ]       

class BusSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Bus
        fields = [
        'id',
        'driver',
        'route',
        'plate',
        'owner'
        ] 

class PassengerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Passenger
        fields = [
        'id',
        'name',
        'last_name',
        'bus',
        'owner'
        ]
class UserSerializer(serializers.ModelSerializer):
    drivers = serializers.PrimaryKeyRelatedField(many=True, queryset=Driver.objects.all())
    routes = serializers.PrimaryKeyRelatedField(many=True, queryset=Route.objects.all())
    buses = serializers.PrimaryKeyRelatedField(many=True, queryset=Bus.objects.all())
    passengers = serializers.PrimaryKeyRelatedField(many=True, queryset=Passenger.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'drivers', 'routes', 'buses', 'passengers']

