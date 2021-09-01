from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class MyShop(models.Model):
    owner   = models.OneToOneField(User,related_name='shop_owner',on_delete=models.CASCADE)
    image   = models.ImageField(upload_to='shop/')
    shop_name   = models.CharField(max_length=120)
    shop_category = models.CharField(max_length=120)
    location    = models.CharField(max_length=120)
    active_shop = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.owner)
