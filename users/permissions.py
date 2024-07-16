from rest_framework import permissions

class IsModer(permissions.BasePermission):

    def has_permission(self, request, view):
        # print (str(request.user.groups.filter(name="moders").exists()))
        print(f"IsModer= {request.user.groups.filter(name='moders').exists()}")
        return request.user.groups.filter(name="moders").exists()