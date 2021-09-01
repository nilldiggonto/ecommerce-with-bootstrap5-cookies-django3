from django.urls import path

from .views import *

urlpatterns = [
    path('',dashboardView,name='dashboard-home'),
    path('create/shop/',createShoView,name='dashboard-create-shop')
]