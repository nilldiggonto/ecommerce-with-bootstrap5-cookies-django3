from django.shortcuts import render,get_object_or_404,redirect
# from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Sum
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

def category(request,slug=None):
    template_name = 'home/category.html'
    product = Products.objects.filter(active=True)
    hotproduct = Products.objects.filter(active=True)
    headline = 'All Items'
    category = None
    all_category =Category.objects.filter(active=True)

    if slug:
        category = get_object_or_404(Category,slug=slug)
        product = category.product.filter(active=True)
        hotproduct = category.product.filter(active=True)
        headline = category.name
    

    page = request.GET.get('page', 1)

    paginator = Paginator(product, 8)
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)

    context = {
        'product':product,
        'headline':headline,
        'category':category,
        'all_category':all_category,
        'hotproduct':hotproduct
        # 'ppages':ppages
    }
    return render(request,template_name,context)


def searchview(request):
    product = None
    query = None
    all_category =Category.objects.filter(active=True)

    if request.method == 'GET':
        query = request.GET.get('isearch')
        product = Products.objects.filter(name__icontains= query,active=True)

        print(query)
    template_name = 'home/search.html'

    page = request.GET.get('page', 1)

    paginator = Paginator(product, 8)
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)
    context = {
        'product':product,
        'query':query,
        'all_category':all_category,
        

    }
    return render(request,template_name,context)
    

def singleView(request,slug=None):
    template_name = 'home/single_page.html'
    all_category =Category.objects.filter(active=True)
    product = None
    if slug:
        product = get_object_or_404(Products,slug=slug)
    context = {
        'all_category':all_category,
        'product':product
    }
    return render(request,template_name,context)

def cartView(request):
    template_name = 'home/cart.html'
    all_category =Category.objects.filter(active=True)
    device = request.COOKIES['device']
    cart = Cart.objects.filter(device=device,consume=False)
    total = cart.aggregate(Sum('total'))
    
    context = {
        'cart':cart,
        'all_category':all_category,
        'total':total

    }
    return render(request,template_name,context=context)


def addCart(request,slug=None):
    device = request.COOKIES['device']
    # print(device)
    item = 1
    if request.method == 'POST':
        item = request.POST.get('cart')
    if slug:
        product = get_object_or_404(Products,slug=slug)
        if Cart.objects.filter(device=device,product=product,consume=False).exists():
            cart = Cart.objects.get(product=product,device=device)
            cart.quantity = cart.quantity + int(item)
            cart.total = cart.total + product.price
            cart.save()
        else:
            Cart.objects.create(device=device,product=product,quantity=int(item),total=product.price * int(item))
        return redirect('cart-page')
    # print(device)
    template_name = 'home/cart.html'
    return render(request,template_name)

def deleteCart(request,id=None):
    cart = Cart.objects.get(pk=id)
    cart.delete()
    
    return redirect('cart-page')
    # 

def checkoutView(request):
    template_name = 'home/checkout.html'
    device = request.COOKIES['device']
    cart = Cart.objects.filter(device=device,consume=False)

    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone   = request.POST.get('phone')
        email   = request.POST.get('email','nomail@noname.com')
        address = request.POST.get('address')
        address_two = request.POST.get('address_two','nothing')
        bkash = request.POST.get('bkash','not')
        cash = request.POST.get('cash','not')
        bkash_no = request.POST.get('bkash_no','not')
        bkash_trans = request.POST.get('bkash_trans','not')

        payment = 'BKASH'
        if cash:
            payment = 'CASH'


        order = Order.objects.create(first_name=fname,
                                        last_name=lname,
                                        phone_no = phone,
                                        email=email,
                                        address= address,
                                        address_two = address_two,
                                        payment=payment,
                                        bkash_no = bkash_no,
                                        bkash_trans = bkash_trans,
                                        device_name= device)
        cart.update(order=order,consume=True)
        return render(request,'home/checkout_done.html')
        # cart.save()

    context = {
        'cart':cart
    }


    return render(request,template_name,context)