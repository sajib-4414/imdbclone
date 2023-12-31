"""user_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,  include
from user_app.grpc_views.validate_handler import grpc_handlers as login_validate_grpc_handlers

servicePrefix = "user-service/"

urlpatterns = [
    path(f"{servicePrefix}admin/", admin.site.urls),
    path(f"{servicePrefix}api/v1/",  include([
        path("account/", include('user_app.api.urls')),
    ])),
    path(f"{servicePrefix}export-app/", include('exports.urls')),
]

def grpc_handlers(server):
    login_validate_grpc_handlers(server)