from django import forms
from .models import Checkout

class Checkoutform(forms.ModelForm):
    name = forms.CharField()
    class Meta:
        model  = Checkout
        fields = ['name', 'email', 'phone', 'address', 'city', 'state', 'payment_method']