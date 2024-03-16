from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.forms import ValidationError

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    
    def clean_password(self):
        user = authenticate(username = self.cleaned_data.get('username'),password= self.cleaned_data.get('password'))
        if user is not None:
            return self.cleaned_data.get('password')
        else:
            raise ValidationError('user is not found',code='invlaid data')
        
        
class RegisterUser(forms.ModelForm):
    class Meta:
        fields = ['username','password']
        model = User
    