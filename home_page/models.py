from django.db import models
from .utils import unique_slugify
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name        = models.CharField(max_length=120,unique=True)
    active      = models.BooleanField(default=True)
    image       = models.ImageField(upload_to='category/',null=True,blank=True)
    slug        = models.SlugField(max_length=300,unique=True,null=True,blank=True)
    feature     = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("category-page", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name
    
    def save(self,**kwargs):
        slug_str = str(self.name)
        unique_slugify(self,slug_str)
        return super().save(**kwargs)

class FeaturedSlide(models.Model):
    title       = models.CharField(max_length=50)
    subtitle    = models.CharField(max_length=100)
    slogan      = models.CharField(max_length=150)
    image       = models.ImageField(upload_to='featured/',null=True,blank=True)
    active      = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Products(models.Model):
    category    = models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)
    name        = models.CharField(max_length=50)
    description = models.TextField()
    image       = models.ImageField(upload_to='product/')
    slug        = models.SlugField(max_length=300,unique=True,null=True,blank=True)
    price       = models.DecimalField(max_digits=5,decimal_places=2)
    avialable   = models.BooleanField(default=True)
    shipping_day    = models.IntegerField()
    weight          = models.DecimalField(max_digits=5,decimal_places=2)
    active          = models.BooleanField(default=True)
    top_sell        = models.BooleanField(default=False)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("single-page", kwargs={"slug": self.slug})
    
    def add_to_cart(self):
        return reverse('add-cart-page', kwargs={'slug':self.slug})

    def __str__(self):
        return self.name
    
    def save(self,**kwargs):
        slug_str = str(self.name)
        unique_slugify(self,slug_str)
        return super().save(**kwargs)



class Order(models.Model):
    device_name = models.CharField(max_length=120,null=True,blank=True)
    first_name  = models.CharField(max_length=120)
    last_name   = models.CharField(max_length=120)
    phone_no    = models.CharField(max_length=120)
    email       = models.EmailField(max_length=120)
    address     = models.TextField()
    address_two = models.TextField()
    payment     = models.CharField(max_length=120)
    bkash_no    = models.CharField(max_length=120,null=True,blank=True)
    bkash_trans = models.CharField(max_length=120,null=True,blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    complete    = models.BooleanField(default=False)

    def __str__(self):
        return str(self.phone_no)

class Cart(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE,related_name='cart')
    order   = models.ForeignKey(Order,related_name='order',on_delete=models.CASCADE,null=True,blank=True)
    device  = models.CharField(max_length=300)
    quantity = models.IntegerField()
    total    = models.DecimalField(max_digits=10,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    consume     = models.BooleanField(default=False)

    def __str__(self):
        return str(self.product)