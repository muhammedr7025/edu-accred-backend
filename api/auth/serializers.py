# apps/management/api/serializers.py

from rest_framework import serializers,validators
from db.models import *

# class UserSerializer(serializers.ModelSerializer):

#     def create(self, validated_data):
#         return CustomUser.objects.create(**validated_data)  
  
#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)  
#         instance.last_name = validated_data.get('last_name', instance.last_name)  
#         instance.email = validated_data.get('email', instance.email)  
#         instance.roll_number = validated_data.get('username', instance.username)  
#         instance.password = validated_data.get('password', instance.password)  
#         instance.user_role = validated_data.get('user_role',instance.user_role)
#         instance.save()  
#         return instance  
#     class Meta:
#         model = CustomUser
#         fields = ['first_name','last_name','email','password','user_role']

# class UserUpdateSerializer(serializers.ModelSerializer):
#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)  
#         instance.last_name = validated_data.get('last_name', instance.last_name)  
#         instance.email = validated_data.get('email', instance.email)  
#         instance.roll_number = validated_data.get('username', instance.username)  
#         instance.password = validated_data.get('password', instance.password)  
#         instance.user_role = validated_data.get('user_role',instance.user_role)
#         instance.save()  
#         return instance  
#     class Meta:
#         model = CustomUser
#         fields = ['first_name','last_name','email','password','user_role']

"""
Obtain Token Serializer
"""
class ObtainTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()