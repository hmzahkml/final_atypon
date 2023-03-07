from rest_framework import serializers
from .models import hotel

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = hotel
        fields = ['manager', 'name', 'maxrooms','stars','address','description']