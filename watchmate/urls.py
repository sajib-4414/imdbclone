
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    #django's built in authentication
    # path("api-auth/", include('rest_framework.urls')),
    path("admin-dashboard/", admin.site.urls),
    path("api/v1/", include([
        path("movies/", include('movie_app.api.urls')),
        path("account/", include('user_app.api.urls')),
    ])),
]
