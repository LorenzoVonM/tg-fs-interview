from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    # Tu código aquí
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'age', 'date_joined']