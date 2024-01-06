from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
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
            # return redirect('/Success_page')    
            return redirect('/')    
    else:
        return render(request, 'login.html')
    
def register_user(request):
    return render(request,'register.html')    

def logout_user(request):
    logout(request)
    messages.success(request,"Successfully Logout")
    return redirect('/')
    # return redirect('home')

