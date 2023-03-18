from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserSerializer, UserUpdateSerializer
from users.permissions import IsAdminOrOwner


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'update':
            self.permission_classes = [IsAdminOrOwner]
            self.serializer_class = UserUpdateSerializer
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [IsAuthenticated]
        elif self.action == 'destroy':
            self.permission_classes = [IsAdminUser]
        return super(self.__class__, self).get_permissions()
