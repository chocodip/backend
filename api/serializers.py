from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User  # ← import your custom model, not from django.contrib.auth.models


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'firstname', 'lastname', 'email', 'password', 'gender']

    def create(self, validated_data):
        # Hash password before saving
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # If password is provided, hash it; otherwise keep existing
        password = validated_data.get('password', None)
        if password:
            validated_data['password'] = make_password(password)
        return super().update(instance, validated_data)
