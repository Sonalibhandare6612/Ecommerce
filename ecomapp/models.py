from django.db import models

# Create your models here.
from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    # Other fields as needed

class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='units')
    type_choices = [('1BHK', '1BHK'), ('2BHK', '2BHK'), ('3BHK', '3BHK'), ('4BHK', '4BHK')]
    type = models.CharField(max_length=4, choices=type_choices)
    rent_cost = models.DecimalField(max_digits=10, decimal_places=2)
    # Other fields as needed

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    agreement_end_date = models.DateField()
    monthly_rent_date = models.PositiveSmallIntegerField()
    # Other fields as needed


# # Model table for Contact information
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    desc=models.TextField(max_length=500)
    phonenumber=models.IntegerField()
    
    
    
    
    def __str__(self):
        return self.name
    
    
           