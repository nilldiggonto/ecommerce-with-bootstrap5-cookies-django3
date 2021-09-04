from django.urls import path
from .views import *

urlpatterns = [
    path('',homeView,name='home-page'),
    path('shop/',category,name='category'),
    path('cart/',cartView,name='cart-page'),
    path('search/',searchview,name='search-page'),
    path('checkout/',checkoutView,name='checkout-view'),
    path('checkout/page/',checkoutDoneView,name='checkout-done-view'),
    path('owner/shop/',owner_shop,name='owner-shop'),


    path('category/<str:slug>/',category,name='category-page'),
    path('item/<str:slug>/',singleView,name='single-page'),
    path('add/cart/<str:slug>/',addCart,name='add-cart-page'),
    path('cart/delete/<int:id>/',deleteCart,name='cart-delete'),
    path('confirm/payment/<int:id>/',confirmPaymentView,name='confirm-payment'),
    path('shop/products/<int:id>/',owner_shop_item_list,name='owner-product-list'),


]
