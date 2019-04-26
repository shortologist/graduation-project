from rest_framework.permissions import BasePermission


class OnlyAdmin(BasePermission):
    """ Allow admin only."""
    def has_permission(self, request, view):
        if request.user == 'admin':
            return True


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return not request.user
