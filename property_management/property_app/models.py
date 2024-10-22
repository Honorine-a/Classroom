
from idlelib.pyshell import usage_msg
from tkinter.constants import UNITS

from django.db import models
# Create your models here.

class Property(models.Model):
    PropertyType = [
        ('Apartment','Apartment'),
        ('House','House'),
        ('Commercial','Commercial'),
    ]

    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    property_type = models.CharField(max_length=50,choices=PropertyType)
    description = models.TextField()
    number_of_units = models.IntegerField()
    def __str__(self):
        return self.name

class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    unit_number = models.CharField(max_length=50)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    rent = models.IntegerField()
    is_available = models.BooleanField(default=True)
    def __str__(self):
     return f'{self.property} - {self.unit_number}'

class Tenant(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Lease(models.Model): # creating lease table
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    rent = models.IntegerField()

    def __str__(self):
            return f'{self.tenant.name}-{self.unit}'
