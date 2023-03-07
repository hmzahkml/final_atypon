from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from utils.decorators.auth import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import hotel
from rest_framework.parsers import JSONParser
from .serializers import HotelSerializer

# Create your views here.


@csrf_exempt
def HotelsApi(request,id=0):
    if request.method=='GET':
        hotell = hotel.objects.all()
        hotel_serializer = HotelSerializer(hotell, many=True)
        return JsonResponse(hotel_serializer.data, safe=False)

    elif request.method=='POST':
        hotel_data=JSONParser().parse(request)
        hotel_serializer = HotelSerializer(data=hotel_data)
        if hotel_serializer.is_valid():
            hotel_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        hotel_data = JSONParser().parse(request)
        hotell=hotel.objects.get(manager=hotel_data['manager'])
        hotel_serializer=HotelSerializer(hotell,data=hotel_data)
        if hotel_serializer.is_valid():
            hotel_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        hotell=hotel.objects.get(manager=id)
        hotell.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

