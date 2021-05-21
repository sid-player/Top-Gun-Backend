import django
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def registerPage(request):
    form=CreateUserForm()
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'User Created for '+ user)
            return redirect('login')
    context={"form":form}
    return render(request,'register.html',context)
def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            messages.info(request,'LOGGED IN')
        else:
            messages.info(request,'Username or Password is incorrect')
           
    context={}
    return render(request,'login.html',context)
def logoutUser(request):
    logout(request)
    return redirect('login')
