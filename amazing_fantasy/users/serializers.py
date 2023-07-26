from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Note, User


class UserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)

    def validate_password(self, password):
        validate_password(password)
        return password

    def create(self, validated_data: dict):
        password = validated_data.pop('password')
        user: User = super().create(validated_data)
        try:
            user.set_password(password)
            user.save()
            return user
        except serializers.ValidationError as exc:
            user.delete()
            raise exc

    class Meta:
        model = User
        fields = ['id', 'first_name', 'username',
                  'country', 'email', 'password']


class NoteSerializer(ModelSerializer):
    author = UserSerializer(read_only=True)
    pub_date = serializers.ReadOnlyField()

    class Meta:
        model = Note
        fields = ['id', 'pub_date', 'author', 'text', ]
