from django.contrib import admin
from .models import *
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display =  ('username', 'items', 'quantity', 'total', 'checkout')
    list_per_page = 10

admin.site.register(Cart, CartAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['username', 'item','price','quantity', 'total', 'status', 'payment_method']
    list_display_links = ['username', 'item','price', 'quantity', 'total', 'status','payment_method']
admin.site.register(OrderItem, OrderItemAdmin)

class WishListAdmin(admin.ModelAdmin):
    list_display = ['username', 'items', 'price']
admin.site.register(WishList, WishListAdmin)
admin.site.register(Contact)

class OrderHistryAdmin(admin.ModelAdmin):
    list_display = ('username', 'item', 'price', 'quantity', 'total', 'paymemnt_method')
    list_display_links = ('username', 'item', 'price', 'quantity', 'total', 'paymemnt_method')
admin.site.register(OrderHistry)

