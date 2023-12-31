from rest_framework import authentication
from django.contrib.auth import get_user_model

class UsernameAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.META.get('HTTP_X_USERNAME')

        if not username:
            return None  # Return None to continue with other authentication classes

        User = get_user_model()
        try:
            user = User.objects.get(username=username)
            return (user, None)
        except User.DoesNotExist:
            return None  # User not found, but it doesn't raise an exception

# In your view, you don't need to manually set request.user
# The custom authentication class will handle it......