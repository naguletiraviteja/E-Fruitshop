from django.shortcuts import render,redirect,get_object_or_404
from fruitshop.models import Fruits
from .models import Cart,Cartitem
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist



def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request,fruit_id):
    fruit = Fruits.objects.get(id=fruit_id)
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save()

    try:
        cartitem = Cartitem.objects.get(fruit=fruit,cart=cart)
        cartitem.quantity +=1
        cartitem.save()
    except Cartitem.DoesNotExist:
        cartitem = Cartitem.objects.create(
            fruit = fruit,
            cart = cart,
            quantity = 1,
        )
        cartitem.save()
    return redirect('cart')


def remove_cart(request,fruit_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    fruit = get_object_or_404(Fruits,id=fruit_id)
    cart_item = Cartitem.objects.get(cart= cart,fruit=fruit)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def remove_cart_totalitems(request,fruit_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    fruit = get_object_or_404(Fruits,id=fruit_id)
    cart_item = Cartitem.objects.get(fruit=fruit,cart=cart)
    cart_item.delete()
    return redirect('cart')

def cart(request,total=0,quantity=0,cart_items=None):
    delivery_charges = 50
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = Cartitem.objects.filter(cart=cart,is_active=True)
        for cart_item in cart_items:
            total += (cart_item.fruit.price * cart_item.quantity)
        total = total + delivery_charges
    except ObjectDoesNotExist:
        pass

    context = {
        "total" : total,
        "quantity" : quantity,
        "cart_items" : cart_items,
        "delivery_charges": delivery_charges,
        "total" : total,
    }

    return render(request,"fruitshop/cart.html",context)



