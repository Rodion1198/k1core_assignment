from rest_framework import serializers

from user.models import UserModel


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ("id", "username", "email")


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ("username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}
