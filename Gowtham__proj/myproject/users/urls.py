from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # Other app-specific URLs for Roles, Rights, etc.
    path('roles/', views.RoleListCreateView.as_view(), name='role-list-create'),
    path('roles/<int:pk>/', views.RoleRetrieveUpdateDestroyView.as_view(), name='role-retrieve-update-destroy'),
    path('rights/', views.RightListCreateView.as_view(), name='right-list-create'),
    path('rights/<int:pk>/', views.RightRetrieveUpdateDestroyView.as_view(), name='right-retrieve-update-destroy'),
    path('members/', views.MemberListCreateView.as_view(), name='member-list-create'),
    path('members/<int:pk>/', views.MemberRetrieveUpdateDestroyView.as_view(), name='member-retrieve-update-destroy'),
]
