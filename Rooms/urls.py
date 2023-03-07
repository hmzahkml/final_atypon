from django.urls import path
from . import views

urlpatterns = [
    path('Rooms/', views.RoomApi, name='Room_api'),
    path('Rooms/<int:id>/', views.RoomApi, name='Room_api_detail'),
]