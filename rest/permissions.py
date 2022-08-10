from rest_framework import permissions


class RestaurantPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):

        if request.method == 'GET':
            return True
        else:
            if obj.user == request.user:
                return True
