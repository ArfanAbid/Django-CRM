from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Record
# Create your views here.

def home(request):
    records=Record.objects.all();        
    return render(request, 'home.html',{'records':records})

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
            return redirect('/')    
            # return redirect('/Success_page')    
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
            return redirect('/')
            # return redirect('/Success_page')    
    else:        
        return render(request,'register.html')    

def logout_user(request):
    logout(request)
    messages.success(request,"Successfully Logout")
    return redirect('/')
    # return redirect('home')

def Record_page(request,pk):
    return render(request,'record_page.html')



def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it=Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"Successfully Deleted record")
        return redirect('/')
    else: 
        messages.success(request,"Please login First !!!")
        return redirect('/')

def add_record(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            address=request.POST.get('address')
            city=request.POST.get('city')
            state=request.POST.get('state')
            zipcode=request.POST.get('zipcode')
            
            add_user=Record.objects.create(first_name=first_name,last_name=last_name,phone=phone,email=email,address=address,city=city,state=state,zipcode=zipcode)
            add_user.save()
            
            messages.success(request,"Successfully registered user ")
            return redirect('/')
        else:
            return render(request,'add_record.html')
    else:
        messages.success(request,"Please login First !!!")
        return redirect('/')




def update_record(request,pk):
    if request.user.is_authenticated:
        update=Record.objects.get(id=pk)
        if request.method == 'POST':
            update.first_name = request.POST.get('first_name')
            update.last_name = request.POST.get('last_name')
            update.email = request.POST.get('email')
            update.phone = request.POST.get('phone')
            update.address = request.POST.get('address')
            update.city = request.POST.get('city')
            update.state = request.POST.get('state')
            update.zipcode = request.POST.get('zipcode')
            update.save()
            
            messages.success(request," Record Updated Successfully !!")
            return redirect('/')
        else:
            return render(request,'update_record.html',{'update':update})
    else:
        messages.success(request,"Please login First !!!")
        return redirect('/')