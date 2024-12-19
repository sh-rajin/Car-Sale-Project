

from django import forms
from .models import CarModel, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'
        

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password ',widget=forms.PasswordInput(attrs={'help_text': None,}))
    password2 = forms.CharField(label='Password Confirmation',widget=forms.PasswordInput(attrs={'help_text': None,}))
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
class ChangeUserData(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','body']