from .models import CustomUser

from rest_framework import serializers

class CustomUserSerializer (serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id',
                  'email',
                  'phone_number',
                  'first_name',
                  'last_name')
