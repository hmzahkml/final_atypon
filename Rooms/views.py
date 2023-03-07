

from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from utils.decorators.auth import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Room
from rest_framework.parsers import JSONParser
from .serializers import RoomSerializer

# Create your views here.


@csrf_exempt
def RoomApi(request,id=0):
    if request.method=='GET':
        Roomm = Room.objects.all()
        Room_serializer = RoomSerializer(Roomm, many=True)
        return JsonResponse(Room_serializer.data, safe=False)

    elif request.method=='POST':
        Room_data=JSONParser().parse(request)
        Room_serializer = RoomSerializer(data=Room_data)
        if Room_serializer.is_valid():
            Room_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        Room_data = JSONParser().parse(request)
        Roomm=Room.objects.get(RoomId=Room_data['RoomId'])
        Room_serializer=RoomSerializer(Roomm,data=Room_data)
        if Room_serializer.is_valid():
            Room_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        Roomm=Room.objects.get(RoomId=id)
        Roomm.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

