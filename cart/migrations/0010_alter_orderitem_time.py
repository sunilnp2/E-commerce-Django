# Generated by Django 4.0.4 on 2022-05-25 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_orderitem_delete_usercart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
