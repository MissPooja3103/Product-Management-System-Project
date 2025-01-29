from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from productapp.models import Product # type: ignore
from django.contrib.auth.decorators import login_required


# Create your views here.

def home_view(request):
    return render(request,'productapp/index.html')


def insert_view(request):
    if request.method == 'POST':
        print(request.POST) 
        product_id=request.POST.get("product_id")
        product_name=request.POST.get("product_name")
        product_price=request.POST.get("product_price")
        product_quantity=request.POST.get("product_quantity")
        obj = Product(product_id=product_id,product_name=product_name,product_price=product_price,product_quantity=product_quantity)
        obj.save()
        print("Product Information Saved Successfully!")
        return redirect('display')
    
    return render(request,'productapp/insert.html')

def display_view(request):
    data= Product.objects.all()
    context = {"data":data}
    return render(request,'productapp/display.html',context)

def delete_view(request,product_id):
   print("in delete view",product_id)
   obj=Product.objects.get(pk=product_id)
   obj.delete()
   return redirect("display")

def update_view(request,product_id):
   print("in update view",product_id)
   obj=Product.objects.get(pk=product_id)

   if request.method == 'POST':
       product_id=request.POST.get("product_id")
       product_name=request.POST.get("product_name")
       product_price=request.POST.get("product_price")
       product_quantity=request.POST.get("product_quantity")
       obj = Product.objects.get(pk = product_id)
       obj.product_id = product_id
       obj.product_name = product_name
       obj.product_price = product_price
       obj.product_quantity = product_quantity
       obj.save()
       return redirect('display')

   return render(request,"productapp/update.html",{'obj':obj})


def register_view(request):
    if request.method == 'POST':
        print(request.POST)
        un = request.POST.get('uname')
        em = request.POST.get('email')
        pwd = request.POST.get('pwd')

        if User.objects.filter(username=un).exists():
            print("User Already Exists")
            return render(request,"productapp/register.html",{'error':"User Already Exists"})
        
        else:
            user = User.objects.create_user(username=un, email=em, password=pwd)
            print("User Created Successfully!")
            return redirect('login')
        
    return render(request,'productapp/register.html')


def login_view(request):
    if request.method == 'POST':
        print(request.POST)
        un = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        user = authenticate(username=un, password=pwd)
        if user is not None:
            login(request, user)
            print("User is now Logged in!")
            print("Authentication Successful!")
            return redirect('index')
        else:
            return render(request,'login.html',{'error' : "Invalid Username or Password"})

    return render(request,'productapp/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
   

