from dataclasses import fields
import numbers
from pyexpat import model
from django import forms
from .models import Item


class ItemsForm(forms.ModelForm):
    catagory = forms.CharField(max_length=120)
    name = forms.CharField(max_length=120)
    price = forms.DecimalField(max_digits=10000, decimal_places=2)
    brand = forms.CharField(max_length=120)
    describtion = forms.Textarea()

    class Meta:
        model = Item
        fields = ['catagory', 'name', 'price', 'brand', 'describtion']


class CartForm(forms.Form):
    name = forms.CharField(max_length=120, widget=forms.TextInput(attrs={
        "readonly": True,
    }))

    price = forms.DecimalField(max_digits=10000, decimal_places=2, widget=forms.NumberInput(attrs = {

        "readonly": True,

    }))
    brand = forms.CharField(max_length=120, widget=forms.TextInput(attrs={
        "readonly": True,

    }))

    number_of_order = forms.IntegerField()
