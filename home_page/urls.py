from django.urls import path
from .views import *

urlpatterns = [
    path('',homeView,name='home-page'),
    path('category/',category,name='category'),
]