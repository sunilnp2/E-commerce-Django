"""ecomm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


# for api router------------------------------------------------
# from rest_framework.routers import DefaultRouter
# from shop.views import ItemModelViewSet, UserModelViewSet
# router = DefaultRouter()

# router.register('itemapi',ItemModelViewSet, basename='itemapi')
# router.register('userapi',UserModelViewSet, basename='userapi')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls', namespace= 'shop')),
    path('cart/', include('cart.urls', namespace= 'cart')),
    # path('khalti/', include('khalti.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('api/', include('shop.api_urls')),
    # url for api ----------------------------------------------
    # path('api/', include(router.urls)),

    # for external api folder-----------------------------
    path('api/', include('api.urls')),
    path('auth/', include('rest_framework.urls', namespace='studapi')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
