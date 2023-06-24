from rest_framework.serializers import ModelSerializer
from .models import Note, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'username', 'country', 'email']


class NoteSerializer(ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Note
        fields = '__all__'



