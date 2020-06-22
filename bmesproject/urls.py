"""
Definition of urls for bmesproject.
"""

from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('', include(('catalogueapp.urls', "catalogueapp"), "catalogueappurls")),
    path('cart/', include(('cartapp.urls', "cartapp"), "cartappurls")),
    path('checkout/', include(('checkoutapp.urls', "checkoutapp"), "checkoutappurls")),

    path('admin/', admin.site.urls),
]
