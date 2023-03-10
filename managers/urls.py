

from django.urls import path, include

from rest_framework_simplejwt.views import (
   
    TokenRefreshView,
)

from .views import LoginView

urlpatterns = [
    
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
