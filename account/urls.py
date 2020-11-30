from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home_page , name = 'home_page'),
    path('sign_up/' , views.signup_page , name = 'sign_up'),
    path('login/' , views.login_page , name = 'login')
]
