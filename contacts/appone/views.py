from django.http import HttpResponse
from django.shortcuts import render,redirect
from appone.forms import Form_one,UploadForm,Userform
from .models import contact
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    contacts = contact.objects.all()  # Fetch all contacts
    return render(request, 'appone/index.html')

def register(request):
    register = False
    if request.method == "POST":
        userform = Userform(data=request.POST)
        uploadform = UploadForm(data=request.POST)


        if userform.is_valid() and uploadform.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()

            profile = uploadform.save(commit=False)
            profile.user = user

            if 'profilepic' in request.FILES:
                profile.profilepic = request.FILES['profilepic']
            profile.save()
            register = True
        else:
            print(userform.errors,uploadform.errors)

    else:
        userform = Userform()
        uploadform = UploadForm()
    
    return render(request,"appone/register.html",context={"userform":userform,"profileform":uploadform,"registered":register})

@login_required
def userlogout(request):
    logout(request)
    return redirect("appone:index")

@login_required
def special(request):
    return render(request,"appone/special.html")

def formview(request):
    form = Form_one()
    if request.method == "POST":
        form = Form_one(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request,"appone/forms.html",context={"form":form})

def deleteall(request):
    contact.objects.all().delete()
    return redirect('appone:index')


# Create your views here.
def userlogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('appone:index')
        else:
            print("error check credentials")

    else:
        return render(request,'appone/login.html')
