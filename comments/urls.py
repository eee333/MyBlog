from django.urls import include, path
from rest_framework import routers

from comments.views import CommentViewSet


comment_router = routers.SimpleRouter()
comment_router.register("comment", CommentViewSet, basename="comment")

urlpatterns = [
    path("", include(comment_router.urls)),
]