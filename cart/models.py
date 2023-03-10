from django.db import models
from fruitshop.models import Fruits

class Cart(models.Model):
    cart_id = models.CharField(max_length=250)
    date_added = models.DateField(auto_now=True)


class Cartitem(models.Model):
    fruit = models.ForeignKey(Fruits,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.fruit.name