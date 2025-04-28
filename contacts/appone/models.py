from django.db import models
from django.contrib.auth.models import User

class Userprofileinfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfoliosite = models.URLField(blank=True)
    profilepic = models.ImageField(upload_to="profilepics",blank=True)


    def __str__(self):
        return self.user.username



   
class contact(models.Model):
    name = models.CharField(max_length=250,unique=True)
    phno = models.CharField(max_length=250,unique=True)
    email = models.EmailField(max_length=250,unique=True,default=None)