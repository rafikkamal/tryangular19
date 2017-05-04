from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    message = ''
    my_safe_method = ['GET', 'PUT', 'DELETE']

    def has_permission(self, request, view):
        if request.method in self.my_safe_method:
            return True
        self.message = 'Not Safe Method'
        return False

    def has_object_permission(self, request, view, obj):

        self.message = 'You must be owner of this object.'
        return obj.user == request.user

