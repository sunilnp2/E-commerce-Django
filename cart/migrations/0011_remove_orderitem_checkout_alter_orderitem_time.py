# Generated by Django 4.0.4 on 2022-05-25 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_alter_orderitem_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='checkout',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
