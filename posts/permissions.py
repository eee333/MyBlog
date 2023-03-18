from rest_framework.permissions import BasePermission


class IsAdminOrOwner(BasePermission):
    message = 'Нет доступа'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author or request.user.is_staff:
            return True
        return False
