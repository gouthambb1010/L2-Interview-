from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permmissions import IsAdmin, IsOperator, IsSuperAdmin, IsTechnician, NoSelfRoleEdit, NoSameRoleDelete, CannotEditOwnRole, CannotDeleteSameRole
from .models import Role, Right, Member
from .serializers import RoleSerializer, RightSerializer, MemberSerializer
from rest_framework.viewsets import ModelViewSet



# Role Views
class RoleListCreateView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]

class RoleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]

# Right Views
class RightListCreateView(generics.ListCreateAPIView):
    queryset = Right.objects.all()
    serializer_class = RightSerializer
    permission_classes = [IsAuthenticated]

class RightRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Right.objects.all()
    serializer_class = RightSerializer
    permission_classes = [IsAuthenticated]

# Member Views
class MemberListCreateView(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]

class MemberRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]

class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated, NoSelfRoleEdit, NoSameRoleDelete, CannotEditOwnRole, CannotDeleteSameRole]

    def get_permissions(self):
        """Set different permissions based on user roles."""
        if self.request.user.role.name == "Super Admin":
            return [IsSuperAdmin()]
        elif self.request.user.role.name == "Admin":
            return [IsAdmin()]
        elif self.request.user.role.name == "Operator":
            return [IsOperator()]
        elif self.request.user.role.name == "Technician":
            return [IsTechnician()]
        return super().get_permissions()
    
    def perform_update(self, serializer):
        # Prevent role update for the logged-in user
        if 'role' in self.request.data and self.request.user == self.get_object():
            raise PermissionDenied("You cannot change your own role.")
        serializer.save()
