from functools import wraps
from django.http import HttpResponseForbidden
import requests

def check_permission(required_permission):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Get the user's username from the request or wherever it's stored...
            username = request.user.username  # Adjust this based on your authentication setup

            # Call the microservice to get user permissions
            response = requests.get(f'http://user-service/get-permissions/{username}/')
            if response.status_code == 200:
                user_permissions = response.json().get('permissions', [])
                if required_permission in user_permissions:
                    # Allow access to the view if the required permission is present
                    return view_func(request, *args, **kwargs)

            # Deny access if the required permission is not present
            return HttpResponseForbidden("You don't have the required permission to access this resource.")

        return _wrapped_view

    return decorator