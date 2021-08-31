from .views import *
from django.urls import path


urlpatterns = [
    path('register/',registrationView,name='auth-register'),
 
    path('login/',loginView,name='auth-login'),
    path('logout/',logoutView,name='auth-logout')

]