from django.urls import path
from exports.views import ExportCreateAPIView,ExportFileView, export_bulk_delete_with_post
urlpatterns = [
    path('exports', ExportCreateAPIView.as_view(), name='export-create-list'),
    path('exports/download/<str:task_id>', ExportFileView.as_view(), name='export-file-download'),
    path('exports/bulk-delete/', export_bulk_delete_with_post, name='export_bulk_delete_with_post'),
]