from rest_framework.permissions import BasePermission


class OrderPermission(BasePermission):

    def get_name(self, request):
        return  request.user.__class__.__name__

    def has_object_permission(self, request, view, obj):
        if self.get_name(request) == 'str' or self.get_name(request) == 'AnonymousUser':
            return False
        else:
            return obj.client == request.user or obj.driver == request.user

    def has_permission(self, request, view):
        if self.get_name(request) == 'str' or self.get_name(request) == 'AnonymousUser':
            return False
        else:
            return request.method == 'GET' or request.method in ('POST', 'PUT') and self.get_name(request) == 'Client'
