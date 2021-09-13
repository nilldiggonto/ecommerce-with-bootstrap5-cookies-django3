from django.db import models
from django.contrib.auth.models import User
from home_page.utils import unique_slugify

# Create your models here.
class MyShop(models.Model):
    owner   = models.OneToOneField(User,related_name='shop_owner',on_delete=models.CASCADE)
    # slug    = models.SlugField()
    slug        = models.SlugField(max_length=300,unique=True,null=True,blank=True)

    image   = models.ImageField(upload_to='shop/',null=True,blank=True)
    shop_name   = models.CharField(max_length=120)
    shop_category = models.CharField(max_length=120)
    location    = models.CharField(max_length=120)
    contact_no  = models.CharField(max_length=120,null=True,blank=True)
    bkash_no  = models.CharField(max_length=120,null=True,blank=True)

    active_shop = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now_add=True)

    def save(self,**kwargs):
        slug_str = str(self.shop_name)
        unique_slugify(self,slug_str)
        return super().save(**kwargs)

    def __str__(self):
        return str(self.owner)
