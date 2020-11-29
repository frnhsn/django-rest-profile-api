from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """ Allow user to edit their own project """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj == request.user

class UpdateOwnFeed(permissions.BasePermission):
    """ Allow user to edit their own project """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
            
        # Instance must have an attribute named `owner`.
        return obj.user == request.user