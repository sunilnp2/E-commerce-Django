from django.urls import path
from .views import *
app_name = 'cart'

urlpatterns = [
        path('add-to-cart/<slug>',add_to_cart,name = 'add-to-cart'),
    ]