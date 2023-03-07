
#rooms model
from django.db import models

from Hotels.models import hotel

# Create your models here.

class Room(models.Model):
   ROOM_TYPES = (
      ('single', 'Single'),
      ('double', 'Double'),
      ('suite', 'Suite')
   )
   RoomId = models.IntegerField(primary_key=True)
   number = models.IntegerField()
   available = models.IntegerField()
   type = models.CharField(max_length=10, choices=ROOM_TYPES)
   description = models.TextField(blank=True)
   price = models.DecimalField(max_digits=6, decimal_places=2)
   hotel = models.ForeignKey(hotel, on_delete=models.CASCADE,related_name='hotel_hotel')