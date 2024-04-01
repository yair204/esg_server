from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'title', 'amount', 'location', 'description', 'product_Img']  
