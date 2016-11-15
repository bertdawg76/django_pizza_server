from django.contrib.auth import get_user_model

from .models import Size, Crust, Topping, Order, Sides, SideNumber
from rest_framework import serializers



User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size


class CrustSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crust


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order

class SidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sides

class SideNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = SideNumber
