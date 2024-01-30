from django.shortcuts import render, redirect
from django_form.form import Registration 
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout



def Mylogin(request):

    if request.method == 'POST':
         username= request.POST['username']
         password= request.POST['password']

         user= auth.authenticate(username= username,password= password)


         if user is not None:
            auth.login(request,user)
            messages.add_message(request,messages.SUCCESS,"Login Successful")
            return redirect('/home')
         else:
            messages.add_message(request,messages.ERROR,"User does not exists",extra_tags="danger")
            return render( request,"home.html")   
    return render(request,"login.html")

def Myregistration(request):
     form= Registration()

     if request.method== "POST":
          form=Registration(request.POST)

          if form.is_valid():
               first_name= request.POST.get('first_name')
               last_name= request.POST.get('last_name')
               username= request.POST.get('username')
               email= request.POST.get('email')
               password= request.POST.get('password')
               confirm_password= request.POST.get('confirm_password')
               user= User.objects.create_user(username=username,first_name= first_name,last_name= last_name,email= email,password=password,is_active= True)
               user.save()
     context= {
      "form": Registration()
     }

     return render(request,"registration.html",context)

@login_required(login_url='/')
def myhome(request):
    if request.method == "GET":
        if request.user.is_authenticated:
          return render(request, "home.html")

def Logout(request):
    
     auth.logout(request)
     return render(request,"login.html")


