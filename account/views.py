from django.shortcuts import render, redirect
from .models import Account
from persiantools.jdatetime import JalaliDate
from .forms import RegisterForm
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth import authenticate, login , logout

# Create your views here.

def home_page(request):
    return render(request, 'account/home.html')


def profile_page(request):
    pass


def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request , username = username , password = password)

        if user is not None:
            login(request, user)
            return redirect('home_page')
    return render(request, 'account/log_in.html')


def signup_page(request):
    register_form_obj = RegisterForm()
    register_form_obj.fields['username'].widget.attrs.update({
        'placeholder' : 'Username'
    })
    register_form_obj.fields['email'].widget.attrs.update({
        'placeholder' : 'Email'
    })
    register_form_obj.fields['password1'].widget.attrs.update({
        'placeholder' : 'Password'
    })
    register_form_obj.fields['password2'].widget.attrs.update({
        'placeholder' : 'Re enter your password'
    })
    context = {
        'form': register_form_obj,
    }
    return render(request, 'account/sign_up.html', context)


def podcart_page(requests):
    pass




