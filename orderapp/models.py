from django.db import models
from userapp.models import Customer
from locationapp.models import Address
from catalogueapp.models import Product

# Base Model
class Base(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta: 
        abstract = True

# Order Model
class Order(Base):

    Order_Status = [(0,"Canceled"),(1,"Submitted"),(2,"Completed"),(3,"Processing")]

    order_total = models.DecimalField(max_digits=9,decimal_places=2)
    order_item_total = models.DecimalField(max_digits=9,decimal_places=2) 
    shipping_charge = models.DecimalField(max_digits=9,decimal_places=2, default=0.00)
    delivery_address = models.OneToOneField(Address,on_delete=models.CASCADE)
    order_status  = models.IntegerField(choices=Order_Status, default=1)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:           
        db_table = 'orders'           
        ordering = ['created_date']

# Order Item Model
class OrderItem(Base):
    quantity = models.IntegerField(default=1)  
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:           
        db_table = 'order_items'           
        ordering = ['created_date']

     
    def total(self):         
        return self.quantity * self.price

    def sku(self):         
         return self.product.sku 
 
    def __str__(self):         
        return '{} ({})'.format(self.product.name,self.product.sku) 
    
    def get_absolute_url(self):         
        return self.product.get_absolute_url()



