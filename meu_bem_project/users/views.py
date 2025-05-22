from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CustomUserSerializer

User = get_user_model()

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

@api_view(['GET'])
def api_root(request):
    return Response({
        "create_user": "/api/users/"
    })
