#hotels model
from django.db import models
# Create your models here.

from managers.models import managersm

class hotel(AbstractUser):
    manager = models.OneToOneField(managersm,on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=50)
    maxrooms = models.IntegerField()
    availablerooms = models.IntegerField()
    stars = models.IntegerField()
    description = models.TextField(blank=True)





#rooms model
from django.db import models

from hotels.models import hotel

# Create your models here.

class Room(models.Model):
    ROOM_TYPES = (
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite')
    )

    number = models.IntegerField()
    type = models.CharField(max_length=10, choices=ROOM_TYPES)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    hotel = models.ForeignKey(hotel, on_delete=models.CASCADE)