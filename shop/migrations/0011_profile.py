# Generated by Django 4.0.4 on 2022-06-06 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_item_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pp', models.ImageField(upload_to='media')),
            ],
        ),
    ]
