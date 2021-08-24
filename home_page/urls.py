from django.urls import path
from .views import *

urlpatterns = [
    path('',homeView,name='home-page'),
    path('shop/',category,name='category'),
    path('item/',singleView,name='single-page'),
]