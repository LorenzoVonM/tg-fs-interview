from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

class UserListAPIView(APIView):
    def get(self, request):
        min_age = request.GET.get("min_age", None)
        if min_age:
            users = User.objects.filter(min_age__gte=min_age).order_by('-date_joined')
        else:
            users = User.objects.order_by('-date_joined')  # Tu lógica aquí

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)