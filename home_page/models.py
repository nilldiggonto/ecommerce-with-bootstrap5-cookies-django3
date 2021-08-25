from django.db import models
from .utils import unique_slugify
# Create your models here.
class Category(models.Model):
    name        = models.CharField(max_length=120,unique=True)
    active      = models.BooleanField(default=True)
    image       = models.ImageField(upload_to='category/',null=True,blank=True)
    slug        = models.SlugField(max_length=300,unique=True,null=True,blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

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