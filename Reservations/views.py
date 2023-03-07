

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required
from .models import reservation
from rest_framework.parsers import JSONParser
from .serializers import reservationSerializer,reservationDeSerializer

# Create your views here.


@csrf_exempt
def ReservationApi(request,id):
    if request.method=='GET':
        reservationn = reservation.objects.get(reservationId=id)
        reservation_serializer = reservationSerializer(reservationn, many=True)
        return JsonResponse(reservation_serializer.data, safe=False)

    elif request.method=='POST':
        reservation_data=JSONParser().parse(request)
        reservation_serializer = reservationDeSerializer(data=reservation_data)
        if reservation_serializer.is_valid():
            reservation_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        reservation_data = JSONParser().parse(request)
        reservationn=reservation.objects.get(id=reservation_data['reservationId'])
        reservation_serializer=reservationSerializer(reservationn,data=reservation_data)
        if reservation_serializer.is_valid():
            reservation_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        reservationn=reservation.objects.get(reservationId=id)
        reservationn.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

