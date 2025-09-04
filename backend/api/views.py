from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

# Create your views here.

# DRF view itself handles the POST request, validation, and user creation
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() # here queryset equals to all users, django will use this to check if user already exists
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Allow any user (authenticated or not) to access this view