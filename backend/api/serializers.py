from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {
            'id': {'read_only': True},
            'username': {'required': True},
            'password': {'write_only': True, 'required': True}
        }
        
        def create(self, validated_data):
            print("Creating user with data:", validated_data)
            user = User.objects.create_user(**validated_data)
            return user