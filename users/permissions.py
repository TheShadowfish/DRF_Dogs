from rest_framework import permissions

class IsModer(permissions.BasePermission):
    """Проверяет является ли пользователь модератором"""

    def has_permission(self, request, view):
        # print (str(request.user.groups.filter(name="moders").exists()))
        # print(f"IsModer= {request.user.groups.filter(name='moders').exists()}")
        return request.user.groups.filter(name="moders").exists()

class IsOwner(permissions.BasePermission):
    """Проверяет является ли пользователь владельцем"""

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False