from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from home_page.models import *
# Create your views here.
@login_required(login_url='/auth/login/')
def dashboardView(request):
    template_name = 'dashboard/dashboard_home.html'

    return render(request,template_name)

@login_required(login_url='/auth/login/')
def createShoView(request):
    template_name = 'dashboard/create_shop.html'

    if request.method == 'POST':
        shopname = request.POST.get('shopname')
        shoptype = request.POST.get('shoptype')
        shopaddress = request.POST.get('shopaddress')
        image = request.FILES['pic']

        user = User.objects.get(username=request.user.username)
        MyShop.objects.create(owner=user,image=image,shop_name=shopname,shop_category=shoptype,location=shopaddress)
        return redirect('dashboard-home')


    return render(request,template_name)

@login_required(login_url='/auth/login/')
def myShopView(request):
    user = User.objects.get(username=request.user.username)
    template_name = 'dashboard/my_shop.html'

    context = {
        'user':user,
    }

    return render(request,template_name,context)


@login_required(login_url='/auth/login/')
def addProductView(request):
    user = User.objects.get(username=request.user.username)
    template_name = 'dashboard/add_product.html'

    category = Category.objects.filter(active=True)

    context ={
        'category':category,
    }
    return render(request,template_name,context)

