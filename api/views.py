from django.shortcuts import render
from django.views.generic import View
from rest_framework import viewsets
from shop.models import *
from api.serializers import *
class ReviewModelViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer