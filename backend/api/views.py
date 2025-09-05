from rest_framework import generics

from .models import Note
from .serializers import UserSerializer, NoteSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.
# List of notes
class NoteListView(generics.ListAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view

# List notes of the authenticated user      
class UserNotesListView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # DRF already validates the serializer
        
class NoteDeleteView(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

# DRF view itself handles the POST request, validation, and user creation
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() # here queryset equals to all users, django will use this to check if user already exists
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Allow any user (authenticated or not) to access this view