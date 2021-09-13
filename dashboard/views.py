from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from home_page.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
        contact_no = request.POST.get('phone_no')
        bkash_no = request.POST.get('bkash')

        user = User.objects.get(username=request.user.username)
        MyShop.objects.create(owner=user,image=image,shop_name=shopname,shop_category=shoptype,location=shopaddress,contact_no=contact_no,bkash_no=bkash_no)
        return redirect('dashboard-home')


    return render(request,template_name)

@login_required(login_url='/auth/login/')
def editShop(request):
    template_name = 'dashboard/create_shop.html'
    user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        shopname = request.POST.get('shopname')
        shoptype = request.POST.get('shoptype')
        shopaddress = request.POST.get('shopaddress')
        
        contact_no = request.POST.get('phone_no')
        bkash_no = request.POST.get('bkash')
        try:
            image = request.FILES['pic']
            user.shop_owner.image = image
        except:
            pass
        user.shop_owner.shop_name = shopname
        user.shop_owner.shop_category = shoptype
        user.shop_owner.location = shopaddress
        user.shop_owner.contact_no = contact_no
        user.shop_owner.bkash_no = bkash_no
        user.shop_owner.save()
        return redirect('dashboard-shop')
    return render(request,template_name,{'user':user})


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
    shop_owner = True
    if user.is_superuser :
        shop_owner = False

    category = Category.objects.filter(active=True)

    if request.method == 'POST':
        category = request.POST.get('category')
        product_name = request.POST.get('pname')
        description = request.POST.get('description')
        
        image = request.FILES['pic'] or None
        
        current_price = request.POST.get('currentprice')
        past_price = request.POST.get('pastprice') or None
        avialable= request.POST.get('available')
        top = request.POST.get('top')
        shipday = request.POST.get('shipday')
        weight = request.POST.get('weight') or None
        cat = Category.objects.get(name=category)
        if avialable == 'on':
            avialable = True
        else:
            avialable = False

        if top == 'on':
            top = True
        else:
            top = False

        
        # print(cat)
        print(avialable)

        Products.objects.create(added_by=user,
                                category =cat,
                                name= product_name,
                                description= description,
                                price =current_price,
                                past_price=past_price,
                                image =image,
                                avialable=avialable,
                                shipping_day = shipday,
                                weight=weight,
                                top_sell = top,shop_owner=shop_owner)
        return redirect('dashboard-product-list')


    context ={
        'category':category,
        'title':'পণ্য যোগ করুন'
    }
    return render(request,template_name,context)

@login_required(login_url='/auth/login/')
def product_list(request):
    template_name = 'dashboard/your_product.html'
    user = request.user
    return render(request,template_name,{'user':user})

@login_required(login_url='/auth/login/')
def edit_product(request,id):
    template_name = 'dashboard/add_product.html'
    user = request.user
    product = Products.objects.get(pk=id)
    shop_owner = True
    if user.is_superuser :
        shop_owner = False
    category = Category.objects.filter(active=True)

    if request.method == 'POST':
        category = request.POST.get('category')
        product_name = request.POST.get('pname')
        description = request.POST.get('description')
        try:
            image = request.FILES['pic']
        except:
            image = None
        current_price = request.POST.get('currentprice')
        past_price = request.POST.get('pastprice')
        avialable= request.POST.get('available')
        top = request.POST.get('top')
        shipday = request.POST.get('shipday')
        weight = request.POST.get('weight')
        cat = Category.objects.get(name=category)
        if avialable == 'on':
            avialable = True
        else:
            avialable = False

        if top == 'on':
            top = True
        else:
            top = False

        
        # print(cat)
        # print(avialable)
        product.category = cat
        product.name = product_name
        product.description = description
        product.price = current_price
        product.past_price =past_price
        if image:
            product.image = image
        product.avialable =avialable
        product.shipping_day = shipday
        product.weight = weight
        product.top_sell = top
        product.save()
        return redirect('dashboard-product-list')
    context = {
        'user':user,
        'product':product,
        'category':category,
        'title':'পণ্য সম্পাদনা করুন'

    }
    return render(request,template_name,context)


@login_required(login_url='/auth/login/')
def order_request_view(request):
    template_name = 'dashboard/order_request.html'
    user = User.objects.get(username=request.user.username)
    # print(user.username)

    orders = Order.objects.filter(shop_owner=user).order_by('-id')
    # print(orders)
    cart = Cart.objects.filter(cart_owner=user)
    if user.is_staff:
        orders = Order.objects.filter(main_shop=True).order_by('-id')
        cart = Cart.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(orders, 15)
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)
    context = {
        # 'all_category':all_category,
        'orders':orders,
        'cart':cart
    }
    return render(request,template_name,context)


