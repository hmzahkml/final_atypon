from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['RoomId', 'number', 'available', 'type', 'description','price','hotel']