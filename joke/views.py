from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == 'POST':
        email =request.POST.get('email')
        username =request.POST.get('username')
        password =request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.info(request,'username exists')
        elif  User.objects.filter(email=email).exists():
            messages.info(request,'email exists') 
        else:
             user = User.objects.create_user(username=username,password=password,email=email)
             user.save()
             return redirect("/login")
    return render(request,'index.html')

def login(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['psw']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("home")
        else:
            messages.info(request,'invalid username or passsword')
            return redirect('login')


    return render(request,'login.html')

def home(request):
    return render(request,'home.html')

