from django.urls import path

from .views import *

urlpatterns = [
    path('',dashboardView,name='dashboard-home'),
    path('create/shop/',createShoView,name='dashboard-create-shop'),
    path('my/shop/',myShopView,name='dashboard-shop'),
    path('add/product/',addProductView,name='dashboard-add-product')
]