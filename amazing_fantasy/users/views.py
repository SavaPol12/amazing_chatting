from rest_framework.decorators import action
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Note, User
from .permissions import IsAuthorOrReadOnly, UserPermission
from .serializers import NoteSerializer, UserSerializer


class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        return serializer.save(author=user)


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthorOrReadOnly, UserPermission]

    def get_queryset(self):
        queryset = User.objects.all()
        country: str = self.request.query_params.get('country')
        if country:
            country = country.title()
            queryset = queryset.filter(country__istartswith=country)
        return queryset

    @action(
        methods=['get', ],
        detail=False,
        url_path='profile'
    )
    def get_profile(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
