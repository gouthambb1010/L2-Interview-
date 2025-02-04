from rest_framework import serializers
from .models import Role, Right, Member

# Serializer for the Right Model
class RightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Right
        fields = ['id', 'name']  # Include the fields to be serialized

# Serializer for the Role Model
class RoleSerializer(serializers.ModelSerializer):
    # Nested RightSerializer to show rights associated with a role
    rights = RightSerializer(many=True, read_only=True)

    class Meta:
        model = Role
        fields = ['id', 'name', 'rights']  # Include the fields to be serialized

# Serializer for the Member Model
class MemberSerializer(serializers.ModelSerializer):
    # Display the role of the member using RoleSerializer
    role = RoleSerializer(read_only=True)

    class Meta:
        model = Member
        fields = ['id', 'username', 'email', 'role']  # Include the fields to be serialized
