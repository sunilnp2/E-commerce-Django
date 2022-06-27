from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import *
router = DefaultRouter()

router.register('itemapi', ItemModelViewSet, basename ='itemapi')
router.register('userapi', UserModelViewSet, basename= 'userapi')
router.register('reviewapi',ReviewModelViewSet, basename='reviewapi')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]
