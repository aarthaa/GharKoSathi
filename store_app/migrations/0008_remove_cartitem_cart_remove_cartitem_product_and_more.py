# Generated by Django 4.2.7 on 2024-02-17 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0007_cart_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]