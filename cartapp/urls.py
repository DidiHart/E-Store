from django.urls import path
from cartapp import views


urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
]
