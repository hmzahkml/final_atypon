from django.shortcuts import render

from rest_framework_simplejwt.views import TokenObtainPairView 


from .models import managersm

from .serializers import CustomTokenObtainPairSerializer



class LoginView(TokenObtainPairView):

    serializer_class =CustomTokenObtainPairSerializer