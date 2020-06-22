from django.contrib import admin
from catalogueapp.models import Product, Category, Brand
from catalogueapp.forms import BrandAdminForm, CategoryAdminForm, ProductAdminForm

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
     form = ProductAdminForm 
  
     list_display = ('name', 'price', 'old_price', 'created_date', 'modified_date',)      
     list_display_links = ('name',)      
     list_per_page = 50      
     ordering = ['-created_date'] 
     search_fields = ['name', 'description', 'meta_keywords', 'meta_description']      
     exclude = ('created_date', 'modified_date',) 
   
     prepopulated_fields = {'slug' : ('name',)} 
     


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin): 
      form = CategoryAdminForm 
   
      list_display = ('name', 'created_date', 'modified_date',)      
      list_display_links = ('name',)      
      list_per_page = 20      
      ordering = ['name']      
      search_fields = ['name', 'description', 'meta_keywords', 'meta_description']      
      exclude = ('created_date', 'modified_date',)           
    
      prepopulated_fields = {'slug' : ('name',)}      



@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin): 
      form = BrandAdminForm 
   
      list_display = ('name', 'created_date', 'modified_date',)      
      list_display_links = ('name',)      
      list_per_page = 20      
      ordering = ['name']      
      search_fields = ['name', 'description', 'meta_keywords', 'meta_description']      
      exclude = ('created_date', 'modified_date',)           
    
      prepopulated_fields = {'slug' : ('name',)}  