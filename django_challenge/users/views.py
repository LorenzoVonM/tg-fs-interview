from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

class UserListAPIView(APIView):
    def get(self, request):
        users = User.objects.all()  # Tu lógica aquí
        #Obtenemos el campo min_age
        min_age = request.query_params.get('min_age')
        if min_age:
            try:
                # Se trata de convertir a entero para asegurar que sea un valor numerico
                min_age =int(min_age)
                # Se realiza el filtrado para los que son mayor o igual a la edad minima
                users.filter(age__gte = min_age)
            except ValueError:
                return Response({'error': 'Parametro min_age invalido'}, status=400)    
        #Se ordena por el más reciente al más antiguo
        users.order_by('-date_joined')    
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)