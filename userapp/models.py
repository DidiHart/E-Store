from django.db import models
from locationapp.models import Address
import datetime

# Base Model
class Base(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta: 
        abstract = True

# Person Model
class Person(Base):
    Gender_Types = [('M', 'Male'),('F', 'Female'),('U', 'Unknown')]
    first_name = models.CharField(max_length=50, unique=False)
    middle_name  = models.CharField(max_length=50,blank=True)  
    last_name = models.CharField(max_length=50, unique=False)
    email_address  = models.EmailField(max_length=50)  
    phone_number = models.CharField(max_length=20, blank=True)
    gender  = models.CharField(max_length=1,choices=Gender_Types,default='U') 
    date_of_birth = models.DateField(default=datetime.date.today)

    class Meta:           
        db_table = 'people'           
        ordering = ['created_date'] 

# Customer Model
class Customer(Base):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True,)
    addresses = models.ManyToManyField(Address)

    class Meta:           
        db_table = 'customers'           
        ordering = ['created_date'] 

