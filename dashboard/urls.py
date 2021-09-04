from django.urls import path

from .views import *

urlpatterns = [
    path('',dashboardView,name='dashboard-home'),
    path('create/shop/',createShoView,name='dashboard-create-shop'),
    path('my/shop/',myShopView,name='dashboard-shop'),
    path('add/product/',addProductView,name='dashboard-add-product'),
    path('product/list/',product_list,name='dashboard-product-list'),
    path('product/edit/<int:id>/',edit_product,name='dashboard-product-edit')
]