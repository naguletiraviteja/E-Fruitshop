# Generated by Django 4.1.4 on 2023-01-04 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruitshop', '0003_remove_fruits_add_to_cart_fruits_is_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruits',
            name='stock',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
