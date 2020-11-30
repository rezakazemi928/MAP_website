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
    acc_obj = Account()

    if request.method == 'POST':
        register_form_obj = RegisterForm(request.POST)

        try:

            if register_form_obj.is_valid():
                first_name_acc = register_form_obj.cleaned_data['first_name']
                last_name_acc = register_form_obj.cleaned_data['last_name']
                email_acc = register_form_obj.cleaned_data['email']
                username_acc = register_form_obj.cleaned_data['username']
                password1_acc = register_form_obj.cleaned_data['password1']
                password2_acc = register_form_obj.cleaned_data['password2']

                if password2_acc == password1_acc:
                    acc_obj.registration_date = str(JalaliDate.today())
                    acc_obj.first_name = first_name_acc
                    acc_obj.last_name = last_name_acc
                    acc_obj.email_address = email_acc
                    acc_obj.username = username_acc
                    acc_obj.password = make_password(password1_acc)
                    acc_obj.save()
                    messages.success(request , 'You account has been created, welcome to our community.')

                    return redirect('login')

                else:
                    messages.error(request, 'The passwords are not matched')

        except IntegrityError:
            account_object_querysets = Account.objects.annotate()

            for i in account_object_querysets:

                if email_acc == i.email_address:
                    messages.error(request , 'The email has already taken')

                if username_acc == i.username:
                    messages.error(request , 'The username has already taken')

    context = {
        'form': register_form_obj,
    }
    return render(request, 'account/sign_up.html', context)


def podcart_page(requests):
    pass




