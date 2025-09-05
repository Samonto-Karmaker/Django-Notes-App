from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # For a ForeignKey (one-to-many), use 'notes' to access all notes of a user (user.notes.all()).
    # For a OneToOneField (one-to-one), use 'note' to access the user's note (user.note).
    # For a ManyToManyField (many-to-many), use 'notes' to access all notes of a user and 'authors' to access all authors of a note.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return self.title