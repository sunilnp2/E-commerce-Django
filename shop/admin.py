from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(Slider)
admin.site.register(Ad)
admin.site.register(Brand)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name' , 'price' , 'category')
    list_display_links = ('name', 'price', 'category')
    list_per_page = 10
    ordering = ['name']
admin.site.register(Item,ItemAdmin)
admin.site.register(Review)
admin.site.register(Profile)
