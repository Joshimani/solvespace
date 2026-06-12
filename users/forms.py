from django import forms
from .models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User

        fields = [
            'full_name',
            'username',
            'profile_pic',
            'email',
            'address',
            'bio',
            'password'

        ]
    

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
