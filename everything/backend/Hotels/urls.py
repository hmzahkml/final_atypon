from django.urls import path
from . import views

urlpatterns = [
    path('hotels/', views.HotelsApi, name='hotels_api'),
    path('hotels/<int:id>/', views.HotelsApi, name='hotels_api_detail'),
]