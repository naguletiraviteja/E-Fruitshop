from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .forms import Forms



# Create your views here.
def register(request):
    form = Forms()
    if request.method == "POST":
        form = Forms(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request,"user created successfully")
            login(request,user)
            return redirect("../home")
    context = {"Registrationform": form}
    return render(request,"register_app/userregistration.html",context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect("/home")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username,password=password)
        except:
            messages.error(request,"username doesnot exists")

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.error(request,"username  or password is incorrect")


    return render(request,"register_app/login.html")


def succesful_registration(request):
    return render(request,"register_app/successful_registration.html")

def logoutuser(request):
    logout(request)
    messages.error(request,"Successfully Loggedout")
    return redirect("home")



