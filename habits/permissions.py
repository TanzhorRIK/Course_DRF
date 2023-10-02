from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = 'Вы не являетесь владельцем'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner or request.user.is_staff:
            return True
        return False


class IsModerator(BasePermission):
    message = 'Вы не модератор'

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return False