from django.db import models

# Base Model
class Base(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta: 
        abstract = True

# Address Model
class Address(Base):
    Address_Type = [(0,"Delivery"),(1,"Billing"),(2,"Unknown")]
    name = models.CharField(max_length=50, blank=True)
    address_line_1  = models.CharField(max_length=100)  
    address_line_2 = models.CharField(max_length=100, blank=True)
    city  = models.CharField(max_length=50)  
    state  = models.CharField(max_length=50) 
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    address_type  = models.IntegerField(choices=Address_Type, default=2)

    class Meta:           
        db_table = 'addresses'           
        ordering = ['created_date'] 

