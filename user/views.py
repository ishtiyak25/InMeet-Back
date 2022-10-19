from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from user.models import User
from user.serializers import UserSerializer


def index(request):
    return render(request, 'index.html', {})


# user login check
# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        response = {
            'user_details': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
