# from rest_framework.authtoken.views import obtain_auth_token
from user_app.api.views import registration_for_regular_view,registration_for_creator_view, logout_view, login_validate_view, call_kafka,get_user_permissions
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
from django.urls import path

urlpatterns = [
    # Using rest framework's Token view to get token which creates also token in database
    # using rest framework's obtain_auth_token to authorize and get token
    path("login-validate/", login_validate_view, name='login-validate'),
    path("get-permissions/<str:username>/", get_user_permissions, name='get-user-permissions'),
    # to use this api, no header, pass in the body as {"refresh":refresh_token}
    path("register/regular/", registration_for_regular_view, name='register'),
    path("register/creator/", registration_for_creator_view, name='register'),
    path("kafka-test/", call_kafka, name='kafka'), #for testing only
    # path("logout/", logout_view, name='logout'),
    
    # jwt authentication token and token refresh
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # # to use api/token call this api with no header, pass username and password in the body
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
