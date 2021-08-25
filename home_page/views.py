from django.shortcuts import render
from .models import *

# Create your views here.
def homeView(request):
    template_name = 'home/home.html'
    category = Category.objects.filter(active=True)
    feature = FeaturedSlide.objects.filter(active=True)
    context = {
        'category':category,
        'feature':feature
    }
    return render(request,template_name,context)

def category(request):
    template_name = 'home/category.html'

    product = Products.objects.filter(active=True)

    context = {
        'product':product
    }
    return render(request,template_name,context)

def singleView(request):
    template_name = 'home/single_page.html'
    return render(request,template_name)

def cartView(request):
    template_name = 'home/cart.html'
    return render(request,template_name)