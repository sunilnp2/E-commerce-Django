from django.db import models
from shop.models import *
from django.core.validators import MaxValueValidator, MinValueValidator 


# Create your models here.
class Cart(models.Model):
    username = models.CharField(max_length=500)
    items = models.ForeignKey(Item,on_delete=models.CASCADE)
    slug = models.CharField(max_length=300)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    total = models.IntegerField()
    checkout = models.BooleanField(default = False)
    grand_total = models.IntegerField(default=0)

    def __str__(self):
        return self.username

class UserCart(models.Model):
    time = models.DateTimeField()
    username = models.CharField(max_length=500)
    items = models.ForeignKey(Item,on_delete=models.CASCADE)
    slug = models.CharField(max_length=300)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    total = models.IntegerField()
    # checkout = models.BooleanField(default = True)
    grand_total = models.IntegerField(default=0)

    def __str__(self):
        return self.username

class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name
