from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirmpassword']:
            try:
                user=User.objects.get(username=request.POST['email'])
                return render(request,'accounts/signup.html',{'error':'Email already exists'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['email'],request.POST['password'])
                auth.login(request,user)
                return redirect('homeurl')
        else:
            return render(request,'accounts/signup.html',{'error':'Password did not match'})
    else:
        return render(request,'accounts/signup.html')

     

def login(request):
     return render(request,'accounts/login.html')

def logout(request):
     return render(request,'accounts/signup.html')