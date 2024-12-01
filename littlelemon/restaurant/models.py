from django.db import models

# Create your models here.
class Booking(models.Model):
    # id = models.IntegerField() # private keys are supplied by default.
    name = models.CharField(max_length=255);
    no_of_guests = models.IntegerField();
    date = models.DateTimeField();
    
class Menu(models.Model):
    # ID->PK
    title = models.CharField(max_length=255);
    price = models.DecimalField(max_digits=10, decimal_places=2); # I assume thats what the 10,2 meant in the screenshot in "Module 2 > Exercise: Settings up the models";
    inventory = models.IntegerField(); # max length might have been intended to be 5. But from the screenshot they sent its unclear.