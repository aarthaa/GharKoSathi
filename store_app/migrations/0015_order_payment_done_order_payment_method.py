# Generated by Django 5.0.2 on 2024-02-21 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0014_order_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Credit Card', 'Credit Card'), ('Debit Card', 'Debit Card'), ('Cash on Delivery', 'Cash on Delivery')], default='Cash on Delivery', max_length=20),
        ),
    ]