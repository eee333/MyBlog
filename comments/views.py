from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from comments.models import Comment
from comments.permissions import IsAdminOrOwner, PermissionPolicyMixin
from comments.serializers import CommentSerializer


class CommentViewSet(PermissionPolicyMixin, ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes_per_method = {
        'create': [IsAuthenticated],
        'update': [IsAdminOrOwner],
        'destroy': [IsAdminOrOwner]
    }
