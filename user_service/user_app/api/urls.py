# from rest_framework.authtoken.views import obtain_auth_token
from user_app.api.views import registration_view, logout_view
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
from django.urls import path

urlpatterns = [
    # Using rest framework's Token view to get token which creates also token in database
    # using rest framework's obtain_auth_token to authorize and get token
    # path("login/", obtain_auth_token, name='login'),
    # to use this api, no header, pass in the body as {"refresh":refresh_token}
    path("register/", registration_view, name='register'),
    # path("logout/", logout_view, name='logout'),
    
    # jwt authentication token and token refresh
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # # to use api/token call this api with no header, pass username and password in the body
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
