from rest_framework import serializers
from shop.models import *
from cart.models import *

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['name', 'profession', 'image', 'discription', 'status']