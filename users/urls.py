from django.urls import include, path
from rest_framework import routers

from users.views import UserViewSet

user_router = routers.SimpleRouter()
user_router.register("user", UserViewSet, basename="user")

urlpatterns = [
    path("", include(user_router.urls)),
]
