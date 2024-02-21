# Generated by Django 5.0.2 on 2024-02-21 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0016_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.TextField(default='x', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.CharField(default=0.0, max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='firstname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='lastname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='images',
            field=models.ImageField(default='', upload_to='Product_images/Order_Img'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='price',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='total',
            field=models.CharField(default='0', max_length=10000),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.CharField(default=0, max_length=20),
        ),
    ]