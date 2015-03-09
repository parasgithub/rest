from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit or view or delete or update it.
    """

    def has_object_permission(self, request, view, obj):
        # Permissions are only given to the owner of the secret.
        return obj.user == request.user
