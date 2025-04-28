from django import forms
from .import models
from django.contrib.auth.models import User


class Form_one(forms.ModelForm):
    
    class Meta:
        model = models.contact
        fields = "__all__"

class Userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ("username","password","email")
    
class UploadForm(forms.ModelForm):
    
    class Meta:
        model = models.Userprofileinfo
        fields = ("profilepic","portfoliosite")

