from django.db import models


class Fruits(models.Model):
    Image = models.ImageField(upload_to="fruit_icons")
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name



    class Meta:
        verbose_name_plural = "Fruits"
