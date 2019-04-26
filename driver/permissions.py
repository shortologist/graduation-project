from rest_framework.permissions import BasePermission


class DriverPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.__class__.__name__ == 'Driver'
