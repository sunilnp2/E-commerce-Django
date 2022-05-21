from django.contrib import admin
from .models import *
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display =  ('username', 'items', 'quantity', 'total', 'checkout')

admin.site.register(Cart, CartAdmin)

class UserCartAdmin(admin.ModelAdmin):
    list_display = ('time', 'username', 'items', 'quantity', 'total')
    list_display_links = ('view')
    def click_me(self,obj):
        return format.html(
            f'<a href = "/admin/{obj.id}">View</a>'
        )
admin.site.register(UserCart)
admin.site.register(Contact)


