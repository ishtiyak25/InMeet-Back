# Serializer to Get User Details using Django Token Authentication
from rest_framework import serializers

from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from user.models import User


# user details serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "fullname", "email", "gender", "phone", "company_name", "company_url", "is_active"]
