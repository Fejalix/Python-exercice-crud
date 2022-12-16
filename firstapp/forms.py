# import form class from django
from django import forms
 
# import Product from models.py
from .models import Product
 
# create a ModelForm
class ProductForm(forms.ModelForm):
    # specify the name of model to use
   class Meta:
        # specify model to be used
        model = Product
 
        # specify fields to be used
        fields = [
            "name",
            "price",
            "quantity",
            "img_url",
        ]