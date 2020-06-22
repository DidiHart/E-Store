from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
from cartapp import cart_service

def cart_detail(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
        cart_service.remove_from_cart(request)

        return render(
        request,
        'cartapp/cart_detail.html',
        {
            'title':'Cart Page',
            'year':datetime.now().year,
        }
      )
    else:
       return render(
        request,
        'cartapp/cart_detail.html',
        {
            'title':'Cart Page',
            'year':datetime.now().year,
        }
      )
