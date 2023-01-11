# Generated by Django 4.1.4 on 2022-12-31 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruitshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fruits',
            options={'verbose_name_plural': 'Fruits'},
        ),
        migrations.AlterField(
            model_name='fruits',
            name='Image',
            field=models.ImageField(upload_to='fruit_icons'),
        ),
        migrations.AlterField(
            model_name='fruits',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]