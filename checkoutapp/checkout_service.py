import uuid
from catalogueapp.models import Product
from cartapp.models import Cart, CartItem
from locationapp.models import Address
from orderapp.models import OrderItem, Order
from userapp.models import Customer, Person
from checkoutapp.forms import CheckoutForm
from django.shortcuts import get_object_or_404
import decimal

UNIQUE_CART_ID_SESSION_KEY = 'unique_cart_id'


# get the current user's unique cart id, sets new one if blank 
def _unique_cart_id(request):
     if request.session.get(UNIQUE_CART_ID_SESSION_KEY,'') == '':            
         request.session[UNIQUE_CART_ID_SESSION_KEY] = _generate_unique_id()    
     return request.session[UNIQUE_CART_ID_SESSION_KEY]


def _generate_unique_id():
    u_id = uuid.uuid1()
    u_id_string = str(u_id)
    return u_id_string

# Gets the cart
def get_cart(request): 
    unique_id =_unique_cart_id(request)
    try:
        cart = get_object_or_404(Cart, unique_cart_id=unique_id)
        return cart
    except :
        return None


# Process checkout
def process_checkout(request):
        form = CheckoutForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            middle_name = form.cleaned_data['middle_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            address_line_1 = form.cleaned_data['address_line_1']
            address_line_2 = form.cleaned_data['address_line_2']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            country = form.cleaned_data['country']
            zip_code = form.cleaned_data['zip_code']
       

            person = Person()
            person.first_name = first_name
            person.middle_name = middle_name
            person.last_name = last_name
            person.email_address = email
            person.save()
          
            address = Address()
            address.address_line_1 = address_line_1
            address.address_line_2 = address_line_2
            address.city = city
            address.state = state
            address.country = country
            address.zip_code = zip_code
            address.save()

            customer = Customer()
            customer.person = person
            customer.save()

            cart = get_cart(request)

            if cart:
               cart_total = get_cart_total(request)

               shipping_cost = decimal.Decimal('0.00')

               order_total = cart_total + shipping_cost

               order = Order()
               order.order_total = order_total   
               order.order_item_total = cart_total
               order.order_status = order.Order_Status[1][0]
               order.shipping_charge = shipping_cost
               order.delivery_address = address
               order.customer = customer
               order.save()

               cart_items = get_cart_items(request)

               if cart_items:
                  for cart_item in cart_items:

                     order_item = OrderItem()
                     order_item.order = order
                     order_item.quantity = cart_item.quantity
                     order_item.price = cart_item.price()
                     order_item.product = cart_item.product
                     order_item.save()
               cart.delete()
               return True       
            else:
               return False


# Return Items From User Cart
def get_cart_items(request):      

    #Get the cart
    cart = get_cart(request)

    if cart:
        return CartItem.objects.filter(cart__unique_cart_id=_unique_cart_id(request))


# Get the Cart Total
def get_cart_total(request):      

    #Get the cart
    cart = get_cart(request)
    cart_total = decimal.Decimal('0.00')

    if cart:
        cart_items = CartItem.objects.filter(cart__unique_cart_id=_unique_cart_id(request))
        for item in cart_items:
            cart_total += item.cart_item_total()
        return cart_total
    else:
        return cart_total

