from django.urls import path
from exports.views import ExportCreateAPIView,ExportFileView
urlpatterns = [
    path('exports', ExportCreateAPIView.as_view(), name='create-new-export'),
    path('exports/download/<str:task_id>', ExportFileView.as_view(), name='export-file-download'),
]