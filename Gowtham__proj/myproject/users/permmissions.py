from rest_framework.permissions import BasePermission
from .models import Role
from rest_framework.exceptions import PermissionDenied


class IsSuperAdmin(BasePermission):
    """Allows access only to Super Admins."""
    def has_permission(self, request, view):
        return request.user.role.name == "Super Admin"


class IsAdmin(BasePermission):
    """Allows access to Admins but restricts deleting Super Admins."""
    def has_permission(self, request, view):
        return request.user.role.name == "Admin"

    def has_object_permission(self, request, view, obj):
        # Admin cannot delete/view Super Admins
        if request.method == "DELETE" and obj.role.name == "Super Admin":
            return False
        return True


class IsOperator(BasePermission):
    """Allows Operators to create/edit Technicians only."""
    def has_permission(self, request, view):
        return request.user.role.name == "Operator"

    def has_object_permission(self, request, view, obj):
        return obj.role.name == "Technician"


class IsTechnician(BasePermission):
    """Technicians can only view their own profile and other technicians."""
    def has_permission(self, request, view):
        return request.user.role.name == "Technician"

    def has_object_permission(self, request, view, obj):
        return obj == request.user or obj.role.name == "Technician"


class NoSelfRoleEdit(BasePermission):
    """Users should not be able to edit their own role."""
    def has_object_permission(self, request, view, obj):
        if request.method in ["PUT", "PATCH"] and obj == request.user:
            return False
        return True


class NoSameRoleDelete(BasePermission):
    """Users should not be able to delete users with the same role."""
    def has_object_permission(self, request, view, obj):
        if request.method == "DELETE" and obj.role == request.user.role:
            return False
        return True
class CannotEditOwnRole(BasePermission):
    """
    Prevent users from changing their own role.
    """
    def has_object_permission(self, request, view, obj):
        if request.user == obj:  # If the logged-in user is trying to edit their own role
            if request.method in ['PATCH', 'PUT']:  # Block role updates
                return False
        return True

class CannotDeleteSameRole(BasePermission):
    """
    Prevent users from deleting another user with the same role.
    """
    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':  # Only apply this rule to delete requests
            if request.user.role == obj.role:  # If the roles are the same
                return False  # Block deletion
        return True