from django.urls import path, include
from rest_framework import routers
from main.user.views import UserViewSet

from main.auth.views import RegisterViewSet, LoginViewSet

# , RefreshViewSet

router = routers.SimpleRouter()

router.register(r"auth/register", RegisterViewSet, basename="auth-register")
router.register(r"auth/login", LoginViewSet, basename="auth-login")
# router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')


router.register(r"user", UserViewSet, basename="user")

urlpatterns = [path("", include(router.urls))]
