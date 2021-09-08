from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import CustomUserViewSet

router_v1 = DefaultRouter()
router_v1.register(r'users', CustomUserViewSet, basename='users')

subscriptions = CustomUserViewSet.as_view({'get': 'subscriptions', })

urlpatterns = [
    path('users/subscriptions/', subscriptions, name='subscriptions'),
    path('', include(router_v1.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
