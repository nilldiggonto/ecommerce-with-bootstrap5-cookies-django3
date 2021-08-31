from django.urls import path

from .views import *

urlpatterns = [
    path('',dashboardView,name='dashboard-home'),
]