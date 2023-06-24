from django.contrib import admin
from django.urls import path, include
from users.views import UserViewSet, NoteViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(
    'users',
    UserViewSet
)
router.register(
    'notes',
    NoteViewSet
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
