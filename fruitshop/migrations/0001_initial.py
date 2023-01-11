# Generated by Django 4.1.4 on 2022-12-31 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fruits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('add_to_cart', models.BooleanField(default=False)),
            ],
        ),
    ]
