from django.db import models

# Base Model
class Base(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta: 
        abstract = True


# Cart Model
class Cart(Base):
    Cart_Status = [(0,"Open"),(1,"CheckedOut")]
    unique_cart_id = models.CharField(max_length=500, unique=False)
    cart_status  = models.IntegerField(choices=Cart_Status, default=0)

    class Meta:           
        db_table = 'carts'           
        ordering = ['created_date'] 

# CartItem Model
class CartItem(Base):
    quantity = models.IntegerField(default=1)      
    product = models.ForeignKey('catalogueapp.Product', unique=False,  on_delete=models.CASCADE) 
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    class Meta:           
        db_table = 'cart_items'           
        ordering = ['created_date'] 
        
    def cart_item_total(self):           
        return self.quantity * self.product.price 
    
    def name(self):           
        return self.product.name  
    
    def price(self):           
        return self.product.price

    def image_url(self):           
        return self.product.image_url

    def get_absolute_url(self):           
        return self.product.get_absolute_url() 
 
    def increase_quantity(self, quantity):           
        self.quantity = self.quantity + int(quantity)           
        self.save()