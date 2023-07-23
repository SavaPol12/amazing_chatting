from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from users.views import NoteViewSet, UserViewSet

router = SimpleRouter()
router.register(
    'users',
    UserViewSet
)
router.register(
    'notes',
    NoteViewSet,

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]


urlpatterns += [
    path('auth/', views.obtain_auth_token),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema')),
]
