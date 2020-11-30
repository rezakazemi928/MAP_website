from .models import Account
from django import forms

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length = 100 , label = 'First Name' , widget = forms.TextInput(attrs = {'placeholder' : 'First Name'}))
    last_name = forms.CharField(max_length = 100 , label = 'Last Name' , widget = forms.TextInput(attrs = {'placeholder' : 'Last Name'}))
    email = forms.EmailField(label = 'Email' , widget = forms.TextInput(attrs = {'placeholder' : 'Email '}))
    username = forms.CharField(max_length = 200 , label = 'Username' , widget = forms.TextInput(attrs = {'placeholder' : 'Username'}))
    password1 = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder' : 'Password'}) ,label = 'Password')
    password2 = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder' : 'Re-enter password'}) , label = 'Re-enter your password')
    profile_pic = forms.FileField(label = 'Your Profile Image' , required = False)

    email.error_messages['unique'] = 'This email has already ben taken'
    username.error_messages['unique'] = 'This username has already be taken '
    class Metta:
        model = Account
        fields = ['first_name' , 'last_name' , 'email' , 'username' , 'password1' , 'password2' , 'profile_pic']


