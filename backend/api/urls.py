from django.urls import path
from .views import NoteListView, UserNotesListView, NoteDeleteView

urlpatterns = [
    path('notes/', NoteListView.as_view(), name='note-list'),
    path('notes/user/', UserNotesListView.as_view(), name='user-notes'),
    path('notes/<int:pk>/', NoteDeleteView.as_view(), name='note-delete'),
]
