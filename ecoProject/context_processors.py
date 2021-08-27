from home_page.models import Cart
from django.db.models import Sum

def cart_count(request):
    device = request.COOKIES['device']
    cart = Cart.objects.filter(device=device,consume=False)
    total = cart.aggregate(Sum('total'))
    return {'cart_count':cart.count(),'cart_total':total}


