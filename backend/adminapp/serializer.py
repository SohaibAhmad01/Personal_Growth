from rest_framework import serializers
from django.contrib.auth.models import User
from .models import User, AdminUser


class UserSerializer(serializers.ModelSerializer):
    class meta:
        models = User
        fields = '__all__'


class AdminUserSerializer(serializers.ModelSerializer):
    class meta:
        model = AdminUser
        fields = '__all__'
