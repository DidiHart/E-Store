from django import forms
from catalogueapp.models import Product, Category, Brand

class ProductAdminForm(forms.ModelForm):
    class Meta:           
        model = Product
        exclude = ('created_date','modified_date')

    def clean_price(self):           
          if self.cleaned_data['price'] <= 0:                
              raise forms.ValidationError('Price must be greater than zero.')           
          return self.cleaned_data['price'] 

class CategoryAdminForm(forms.ModelForm):
    class Meta:           
        model = Category
        exclude = ('created_date','modified_date')

class BrandAdminForm(forms.ModelForm):
    class Meta:           
        model = Brand
        exclude = ('created_date','modified_date')
