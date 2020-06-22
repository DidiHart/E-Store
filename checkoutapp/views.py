from django.shortcuts import render, redirect
from django.http import HttpRequest
from datetime import datetime
from checkoutapp.forms import CheckoutForm
from checkoutapp import checkout_service

def checkout(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
        result  = checkout_service.process_checkout(request)
        if result:
           return redirect('/checkout/receipt')
        else:
           return redirect('/checkout/receipt')
    else:
       form = CheckoutForm()
       return render(
         request,
         'checkoutapp/checkout.html',
         {
            'title':'Checkout Page',
            'year':datetime.now().year,
            'form': form,
         }
      )

def receipt(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    return render(
        request,
        'checkoutapp/receipt.html',
        {
            'title':'Receipt Page',
            'year':datetime.now().year,
        }
      )
