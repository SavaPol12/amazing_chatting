from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.http import HttpRequest


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request: HttpRequest, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user == obj.author:
            return True
        return False