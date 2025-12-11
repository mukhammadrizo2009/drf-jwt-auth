from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    message = "Siz Admin Emassiz!"
    
    def has_permission(self, request, view):
        return request.user and request.user.is_admin
    
class IsUser(BasePermission):
    message = "Siz User Emassiz!"
    
    def has_permission(self, request, view):
        return request.user and request.user.is_user

class IsManager(BasePermission):
    message = "Siz Manager Emassiz!"
    
    def has_permission(self, request, view):
        return request.user and request.user.is_manager