from django.db import models

# Rights Model
class Right(models.Model):
    name = models.CharField(max_length=255)  # Name of the right (e.g., Create User, Edit User)
    
    def __str__(self):
        return self.name


# Roles Model
class Role(models.Model):
    name = models.CharField(max_length=255)  # Name of the role (e.g., Super Admin, Admin)
    rights = models.ManyToManyField(Right, related_name="roles")  # Many-to-many relationship with Rights
    
    def __str__(self):
        return self.name


# Members (Users) Model
class Member(models.Model):
    username = models.CharField(max_length=255, unique=True)  # Username of the member
    email = models.EmailField(unique=True)  # Email of the member
    password = models.CharField(max_length=255)  # Password (ideally hashed)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)  # One-to-many relationship with Role
    
    def __str__(self):
        return self.username
