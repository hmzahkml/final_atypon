
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import managersm

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user: managersm):
        token = super().get_token(user)

        token['name'] = user.username
        token['email'] = user.email
        token['user_id'] = user.id
        return token
