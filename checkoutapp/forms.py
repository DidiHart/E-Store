from django import forms 

class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=50, widget = forms.TextInput(attrs={
                'class': 'form-control checkout__subject-input'
                }))
    middle_name = forms.CharField(max_length=50, required=False, widget = forms.TextInput(attrs={
                'class': 'form-control checkout__subject-input'
                }))
    last_name = forms.CharField(max_length=50, widget = forms.TextInput(attrs={
                'class': 'form-control checkout__subject-input'
                }))
    email = forms.EmailField(widget = forms.TextInput(attrs={
                'class': 'form-control checkout__subject-input'
                }))

    address_line_1 = forms.CharField(max_length=100, widget = forms.TextInput(attrs={
                'class': 'form-control checkout__subject-input'
                }))
    address_line_2 = forms.CharField(max_length=100, required=False, widget = forms.TextInput(attrs={
                'class': 'form-control checkout__subject-input'
                }))
    city = forms.CharField(max_length=50, widget = forms.TextInput(attrs={
                'class': 'form-control checkout__subject-input'
                }))
    state = forms.CharField(max_length=50, widget = forms.TextInput(attrs={
                'class': 'form-control checkout__subject-input'
                }))
    country = forms.CharField(max_length=50, widget = forms.TextInput(attrs={
                'class': 'form-control checkout__subject-input'
                }))
    zip_code = forms.CharField(max_length=50, widget = forms.TextInput(attrs={
                'class': 'form-control checkout__subject-input'
                }))
