from django.urls import path
from . import views

urlpatterns = [
     path("cart/",views.cart,name = "cart"),
    path('add_cart/<int:fruit_id>/',views.add_cart,name='add_cart'),
    path('remove_total_cart/<int:fruit_id>/',views.remove_cart_totalitems,name="remove_total_cart"),
    path('remove_item/<int:fruit_id>',views.remove_cart,name='remove_cart'),

]