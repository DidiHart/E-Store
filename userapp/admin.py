from django.contrib import admin
from userapp.models import Person, Customer
from userapp.forms import CustomerAdminForm, PersonAdminForm

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
     form = PersonAdminForm 
  
     list_display = ('first_name', 'middle_name', 'last_name','email_address','phone_number','gender','date_of_birth', 'created_date', 'modified_date',)      
     list_display_links = ('first_name',)      
     list_per_page = 50      
     ordering = ['-created_date'] 
     search_fields = ['first_name', 'middle_name', 'last_name', 'email_address']      
     exclude = ('created_date', 'modified_date',) 
     

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin): 
      form = CustomerAdminForm 
   
      list_display = ('person',)      
      list_display_links = ('person',)      
      list_per_page = 20      
      ordering = ['-created_date']      
      search_fields = ['person',]      
      exclude = ('created_date', 'modified_date',) 


