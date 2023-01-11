# Generated by Django 4.1.4 on 2023-01-04 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruitshop', '0002_alter_fruits_options_alter_fruits_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fruits',
            name='add_to_cart',
        ),
        migrations.AddField(
            model_name='fruits',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]