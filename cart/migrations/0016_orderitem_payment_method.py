# Generated by Django 4.0.4 on 2022-05-28 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0015_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='payment_method',
            field=models.CharField(choices=[('Pay With Khalti', 'Pay With Khalti'), ('Cash on Delivery', 'Cash on Delivery')], default='Cash on Delivery', max_length=200),
        ),
    ]
