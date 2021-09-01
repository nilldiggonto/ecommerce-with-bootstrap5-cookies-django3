from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ProfileUser(models.Model):
    profile = models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)
    phone   = models.CharField(max_length=120)
    address = models.TextField()
    address_two = models.TextField(null=True,blank=True)
    image   = models.ImageField(upload_to='profile/',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.phone)
    
