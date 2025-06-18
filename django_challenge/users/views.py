from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

class UserListAPIView(APIView):
    def get(self, request):
        # Min age, get the param in the request
        min_age = request.query_params.get('min_age')

        # Filter all user by date_joined field desc
        users = User.objects.all().order_by('-date_joined')

        # if the min_age exist 
        if min_age is not None:
            try:
                min_age = int(min_age)
                users = users.filter(age__gte=min_age)
            except ValueError:
                except Response('error: min_age must be integer', status=400)
        
        serializer = UserSerializer(users, many=True)

        # Get the firts_name and last_name from the request
        first_name = serializer.data['first_name']
        last_name = serializer.data['last_name']
        full_name = first_name + last_name

        # add the full name field to the request
        serializer.data['full_name'] = full_name

        # checking if the age is higher or equals to 18
        age = serializer.data['age']
        if age >= 18:
            is_adult = True
        else:
            is_adult = False

        # Add the is_Adult filed to the request if tre
        serializer.data['is_Adult'] = is_adult

        # count all users to stadistic
        total = users.count()
        sum_age = sum(1 for user in users)

        average_age = sum_age/total

        # New Response
        return Response({
            'average_age': average_age,
            'users': serializer.data
        })
        

        # return Response(serializer.data)
    