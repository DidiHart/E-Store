
"""
Definition of urls for catalogueapp.
"""

from django.urls import path
from catalogueapp import views

urlpatterns = [
    path('', views.catalogue, name='catalogue'),
    path('catalogue/<category_slug>/<brand_slug>/', views.catalogue, name='catalogue'),
    path('catalogue/products/<product_slug>/', views.product_detail, name='product_detail'),
]
