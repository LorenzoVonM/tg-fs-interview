from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    # Tu código aquí
    full_name = serializers. SerializerMethodField()
    is_adult = serializers. SerializerMethodField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'age', 'date_joined', 'full_name', 'is_adult']

    def get_full_name(self, obj):
        #Devuelve el primer nombre seguido del apellido
        return f"{obj.first_name} {obj.last_name}" 

    def get_is_adult(self, obj):
        if obj.age is not None:
            # Si es mayor o igual a 18 retornara True
            return obj.age >= 18
        return False    