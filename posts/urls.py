from django.urls import include, path
from rest_framework import routers

from posts.views import PostViewSet


post_router = routers.SimpleRouter()
post_router.register("post", PostViewSet, basename="post")

urlpatterns = [
    path("", include(post_router.urls)),
]
