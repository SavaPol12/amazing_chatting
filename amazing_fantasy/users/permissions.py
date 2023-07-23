from django.http import HttpRequest
from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request: HttpRequest, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user == obj.author:
            return True
        return False
