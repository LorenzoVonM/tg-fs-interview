from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    is_adult = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    def get_is_adult(self, obj):
        return int(obj.age) >= 18

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'age', 'date_joined']
        read_only_fields = ("is_adult", "full_name")