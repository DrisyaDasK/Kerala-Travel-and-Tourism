from django import forms
from django.contrib.auth.models import User
from travelapp.models import Booking


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password','email']

class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username', 'password']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'UserName'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
        }

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields="__all__"
