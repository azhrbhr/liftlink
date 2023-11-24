# accounts/models.py
from django.contrib.auth.models import User
from django.db import models

FUEL_TYPE_CHOICES = [
    ('petrol', 'Petrol'),
    ('diesel', 'Diesel'),
    ('electric', 'Electric'),
]

TRANSMISSION_CHOICES = [
    ('automatic', 'Automatic'),
    ('manual', 'Manual'),
]

VEHICLE_TYPE_CHOICES = [
    ('car', 'Car'),
    ('truck', 'Truck'),
    ('suv', 'SUV'),
    ('motorcycle', 'Motorcycle'),
]


class Vehicle(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=20)
    registration_number = models.CharField(max_length=15, unique=True)
    license_number = models.CharField(max_length=20)
    capacity = models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=20, choices=FUEL_TYPE_CHOICES)
    transmission = models.CharField(
        max_length=20, choices=TRANSMISSION_CHOICES)
    # current_location = models.PointField()  # Assuming you use a spatial database like PostGIS for this field
    vehicle_type = models.CharField(
        max_length=20, choices=VEHICLE_TYPE_CHOICES)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model} - {self.registration_number}"
