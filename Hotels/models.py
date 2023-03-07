# Create your models here.


#hotels model
from django.db import models
# Create your models here.

from managers.models import managersm

class hotel(models.Model):
    manager = models.OneToOneField(managersm,on_delete=models.CASCADE,primary_key=True, related_name='maneger')
    name = models.CharField(max_length=50)
    maxrooms = models.IntegerField()
    stars = models.IntegerField()
    address = models.CharField(max_length=50)
    description = models.TextField(blank=True)

