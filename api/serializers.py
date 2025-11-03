from rest_framework import serializers
from .models import User  # ← import your custom model, not from django.contrib.auth.models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'firstname', 'lastname', 'email', 'password', 'gender']
