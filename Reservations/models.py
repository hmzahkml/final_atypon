#rooms model
from django.db import models

from Rooms.models import Room

# Create your models here.

class reservation(models.Model):

    reservationId = models.AutoField(primary_key=True)
    reserved_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField()
    offer = models.ForeignKey(Room, on_delete=models.CASCADE,related_name='room')
    email = models.EmailField(blank=False)
    phone_number = models.IntegerField(blank=True)
    number_days= models.IntegerField(blank=False)
    is_canceled= models.BooleanField(default=False)