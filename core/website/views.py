from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    return render(request, 'home.html',{})

def login_user(request):
    if request.method == 'POST':
        user_name=request.POST.get('user_name')
        password=request.POST.get('password')
        
        user=authenticate(username=user_name, password=password)
        if user is None:
            messages.info(request,"Invalid password")
            return redirect('/login')
        else:
            login(request,user)
            messages.success(request,"Successfully Login")
            return redirect('/Success_page')    
            # return redirect('/')    
    else:
        return render(request, 'login.html')
    
def register_user(request):
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        user_name=request.POST.get('user_name')
        password=request.POST.get('password')
        
        if User.objects.filter(username=user_name).exists():
            messages.info(request," User already Exists !!")
            return redirect('/Register')
        else:
            register_user=User.objects.create(username=user_name,first_name=first_name,last_name=last_name)
            register_user.set_password(password)
            register_user.save()
            
            messages.success(request,"Account created Succesfully! ")
            return redirect('/Success_page')    
            # return redirect('/')
    else:        
        return render(request,'register.html')    

def logout_user(request):
    logout(request)
    messages.success(request,"Successfully Logout")
    return redirect('/')
    # return redirect('home')

def Success_page(request):
    return render(request,'success_page.html')