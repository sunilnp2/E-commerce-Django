from django.urls import reverse

from django.db import models

# Create your models here.
STATUS = (('active','active'),('inactive','inactive'))
LABEL = (('new','new'),('hot','hot'),('','default'))




class Category(models.Model):
    name = models.CharField(max_length=200)
    logo = models.CharField(max_length=200)
    slug = models.CharField(max_length=300,unique=True)
    status = models.CharField(choices= STATUS,max_length=200)
    def __str__(self):
        return self.name

class Slider(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to= 'media')
    description = models.TextField()
    status = models.CharField(choices= STATUS,max_length=200)

    def __str__(self):
        return self.name

class Ad(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to= 'media')
    discription = models.TextField(blank=True)
    rank = models.IntegerField()
    status = models.CharField(choices= STATUS,max_length=200)
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to= 'media')
    status = models.CharField(choices= STATUS,max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=400)
    price = models.PositiveBigIntegerField()
    discounted_price = models.PositiveBigIntegerField(default=0)
    image = models.ImageField(upload_to= 'media')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    label = models.CharField(choices= LABEL,max_length=200,blank=True)
    status = models.CharField(choices= STATUS,max_length=200,blank=True)
    discription = models.TextField(blank=True)
    slug = models.CharField(max_length=300,unique=True)
    specification = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def add_to_cart(self):
        return reverse('cart:add-to-cart',kwargs = {'slug':self.slug})

class Review(models.Model):
    name = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    image = models.ImageField(upload_to= 'media')
    discription = models.TextField()
    status = models.CharField(choices= STATUS,max_length=200)

    def __str__(self):
        return self.name


    # model for profile
class Profile(models.Model):
    pp = models.ImageField(upload_to= 'media')
    







