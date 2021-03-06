from django.urls import path
from .views import *
app_name = 'shop'

urlpatterns = [
        path('',HomeView.as_view(),name = 'home'),
        path('category/<slug>',CategoryView.as_view(),name = 'category'),
        path('brand/<name>',BrandView.as_view(),name = 'brand'),
        path('search',ItemSearchView.as_view(),name = 'search'),
        path('item_detail/<slug>',ItemDetailView.as_view(),name = 'item_detail'),
        path('signup', signup,name = 'signup'),
        path('login/', login,name = 'login'),
        path('logout/', logout,name = 'logout'),
        path('profile', profile, name='profile'),
        path('editprofile', editprofile, name = "editprofile"),
        path('change-pass', password_change, name = "change-pass"),
        path('setcookie', setcookie, name = 'setcookie'),
        # path('delcookie', delcookie, name = 'delcookie'),
        path('setsession', setsession,name = 'setsesion'),
        path('delsesion', delsession,name = 'delsesion'),
        # path('checkout', checkout,name = 'checkout'),

]