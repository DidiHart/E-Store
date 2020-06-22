from django.urls import path
from checkoutapp import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('receipt', views.receipt, name='receipt'),
]
