from bmesproject import settings
from catalogueapp.models import Brand, Category
from cartapp import cart_service 

def bmes_context(request):
    return {
              'site_name': settings.SITE_NAME,
              'categories': Category.objects.filter(category_status=0), 
              'brands': Brand.objects.filter(brand_status=0), 
              'selected_category':'all-categories',
              'selected_brand':'all-brands',
              'cart_item_count': cart_service.cart_items_count(request),
              'cart_total': cart_service.get_cart_total(request),
              'cart_items': cart_service.get_cart_items(request),
           }