from django.urls import path
from . import views

urlpatterns = [
    path('Res/', views.ReservationApi, name='Res_api'),
    path('Res/<int:id>/', views.ReservationApi, name='Res_api_detail'),
]