from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'user_role', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            email=validated_data['email'],
            user_role=validated_data['user_role'],
            password=validated_data['password'],
        )
        return user
    