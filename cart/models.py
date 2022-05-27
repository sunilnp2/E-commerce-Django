from distutils.command.upload import upload
from django.db import models
from shop.models import *
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator 
ostatus = (
    ('Pending','Pending'),
    ('Accepted','Accepted'),
  ('On The Way','On The Way'), 
  ('Delivered','Delivered'), 
  ('Cancelled','Cancel'),
  )

# Create your models here.
class Cart(models.Model):
    username = models.CharField(max_length=500)
    items = models.ForeignKey(Item,on_delete=models.CASCADE)
    slug = models.CharField(max_length=300)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=1)
    total = models.IntegerField()
    checkout = models.BooleanField(default = False)
    grand_total = models.IntegerField(default=0)

    def __str__(self):
        return self.username

class WishList(models.Model):
    username = models.CharField(max_length=200)
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
    slug = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=1)

    def __str__(self):
        return self.username


# class UserCart(models.Model):
#     time = models.DateTimeField()
#     username = models.CharField(max_length=500)
#     items = models.ForeignKey(Item,on_delete=models.CASCADE)
#     slug = models.CharField(max_length=300)
#     quantity = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
#     total = models.IntegerField()
#     # checkout = models.BooleanField(default = True)
#     grand_total = models.IntegerField(default=0)

#     def __str__(self):
#         return self.

class OrderItem(models.Model):
    username = models.CharField(max_length=500)
    # phone = models.CharField(max_length=200)
    # add = models.CharField(max_length=200)
    item  = models.ForeignKey(Item,on_delete=models.CASCADE)
    # slug = models.CharField(max_length=300)
    price = models.IntegerField()
    # image = models.ImageField(upload_to = 'media')

    quantity = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    total = models.IntegerField()
    # checkout = models.BooleanField(default = False)
    time = models.DateTimeField(auto_now_add = True)
    status = models.CharField(choices=ostatus, max_length=200,default='Pending')
    


    def __str__(self):
        return self.username
    

class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name
