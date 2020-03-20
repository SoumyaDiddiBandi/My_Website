from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#class profile_pic(models.Model):
 #   image = models.FilePathField(path="home/img")
class Profile(models.Model):
       user=models.OneToOneField(User,on_delete=models.CASCADE)
       image=models.ImageField(default='default.jpg',upload_to='profile_picture')


