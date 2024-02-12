from rest_framework import permissions
import requests
from django.contrib.auth import get_user_model
from django.core.cache import cache
User = get_user_model()

class IsAdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)

class IsReviewUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.review_user == request.user or request.user.is_staff

class IsContentCreatorOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        print("permission checked.....")
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if not request.user.is_authenticated:
                print("came here....")
                return False
            user_role  = request.user.role
            if not user_role or len(user_role)==0:
                #role is not yet created in this movie service, anyway we should not allow without explicit permission.
                return False
            print("user role is",request.user.role)
            if user_role == "REGULAR_USER":
                return False
            
            # Check if the response is already in the cache
            cache_key = f'user_permissions_{request.user.username}'
            cached_permissions = cache.get(cache_key)
            if cached_permissions is not None:
                print("Using cached permissions...")
                return 'user_app.create_content' in cached_permissions
            
            response = requests.get(f'http://user-service:8000/user-service/api/v1/account/get-permissions/{request.user.username}')
            fetched_permissions = response.json().get('permissions', [])
            print(fetched_permissions)
            cache.set(cache_key, fetched_permissions, 300)
            return response.status_code == 200 and 'user_app.create_content' in fetched_permissions
    
