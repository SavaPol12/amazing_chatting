from .models import Note, User
from .serializers import NoteSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated

class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthorOrReadOnly, ]


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]