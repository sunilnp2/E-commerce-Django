from django.urls import path
from .views import *
app_name = 'cart'

urlpatterns = [
        path('add-to-cart/<slug>',addcart,name = 'add-to-cart'),
        # path('user_cart/<slug>', user_cart, name = 'user_cart'),
        path('payment', payment, name = 'payment'),
        path('cart', show_cart,name = 'cart'),
        path('delete_cart/<slug>', delete_cart,name = 'delete_cart'),
        path('increase_cart/<slug>', increase_cart,name = 'increase_cart'),
        path('dec_cart/<slug>', dec_cart,name = 'dec_cart'),
        path('checkout',checkout,name = 'checkout'),
        path('orders/', orders, name='orders'),
        path('add-wishlist/<slug>',add_wishlist, name = "add-wishlist"),
        path('wish-list-inc/<slug>', wish_inc, name = "wish-list-inc"),
        path('wish-list-dec/<slug>', wish_dec, name = "wish-list-dec"),
        path('wish-list-del/<slug>', wish_delete, name = "wish-list-del"),
        path('wishlist', WishListView.as_view(), name='wishlist'),
        path('khalti-pay/', KhaltiPayView.as_view(), name= "khalti-pay"),
    ]