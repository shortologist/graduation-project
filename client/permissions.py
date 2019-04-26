from rest_framework.permissions import BasePermission


class ClientPermission(BasePermission):
    """
    This permission allow client to get and edit his orders,
    and allow any client to make owen order.
    """
    def has_permission(self, request, view):
        if request.user == None and request.method == 'POST':
            return True
        return request.user.__class__.__name__ == "Client"
