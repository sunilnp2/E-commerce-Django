from django.urls import path
from .views import *
app_name = 'cart'

urlpatterns = [
        path('add-to-cart/<slug>',AddCartView.as_view(),name = 'add-to-cart'),
        path('user_cart/<slug>', user_cart, name = 'user_cart'),
        path('cart', CartView.as_view(),name = 'cart'),
        path('delete_cart/<slug>', delete_cart,name = 'delete_cart'),
        path('increase_cart/<slug>', increase_cart,name = 'increase_cart'),
        path('dec_cart/<slug>', dec_cart,name = 'dec_cart'),
        path('checkout',CheckoutView.as_view(),name = 'checkout'),
    ]