from rest_framework import serializers
from .models import reservation

class reservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = reservation
        fields = ['reservationId', 'reserved_at', 'start_date', 'offer', 'email','phone_number','number_days','is_canceled']
        
        
        
class reservationDeSerializer(serializers.ModelSerializer):
    class Meta:
        model = reservation
        fields = ['start_date', 'offer', 'email','phone_number','number_days']