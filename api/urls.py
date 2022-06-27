from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import *
router = DefaultRouter()

router.register('reviewapi',ReviewModelViewSet, basename='reviewapi')


urlpatterns = [
    path('', include(router.urls)),
]
