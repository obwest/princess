from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Account

class LoginForm(forms.ModelForm):
    password    = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('username', 'password')

    def clean(self):
        # cleaned_data = super().clean()
        if self.is_valid():
            username    = self.cleaned_data['username']
            password    = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError('Invalid login')