from django.shortcuts import render
from .models import Fruits

# Create your views here.

def index(request):
    fruit_box = Fruits.objects.all()
    return render(request,"fruitshop/index.html",{
        "fruits" : fruit_box
    })


