
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from drf_spectacular.generators import SchemaGenerator
servicePrefix = "movie-service/"
# Set the WITH_EXTENSIONS setting to enable extensions

urlpatterns = [
    #django's built in authentication
    # path("api-auth/", include('rest_framework.urls')),
    path(f"{servicePrefix}admin-dashboard/", admin.site.urls),
    path(f"{servicePrefix}api/v1/", include([
        path("movies/", include('movie_app.api.urls')),
        # path("account/", include('user_app.api.urls')),
    ])),
    path(f"{servicePrefix}api/schema/", SpectacularAPIView.as_view(), name='schema'),
    path(f"{servicePrefix}api/schema/docs/", SpectacularSwaggerView.as_view(url_name='schema')),
]
