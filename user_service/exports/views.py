import rest_framework.decorators
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
User = get_user_model()
import pandas as pd
import os
from django.http import JsonResponse
from io import BytesIO
from django.core.files.storage import default_storage
from django.shortcuts import get_object_or_404
from exports.models import Export
from django.conf import settings
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from rest_framework import status
from user_app.helpers.serializer_error_parser import create_error_from_message
from exports.tasks import generate_csv_file
from rest_framework.response import Response
from celery.result import AsyncResult
from exports.serializers import ExportSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404
# Create your views here.
class ExportCreateAPIView(APIView):
    permission_classes= [IsAuthenticated]
    def post(self, request, format=None):
        user = request.user
        celery_task = generate_csv_file.delay(user.id)
        Export.objects.create(
            creator=user,
            file_name="",
            description="Registration data, Review Data",
            task_id = celery_task.id
        )
        response_data = {
            'export_id': celery_task.id,
            'status': 'queued',
        }

        return Response(response_data, status=status.HTTP_202_ACCEPTED)
    def get(self, request):
        exports = Export.objects.all()
        serializer = ExportSerializer(exports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def export_bulk_delete_with_post(request):
    export_ids_to_delete  = request.data.get('export_ids', [])
    exports_to_delete = get_list_or_404(Export, id__in=export_ids_to_delete) #Export.objects.filter(id__in=export_ids_to_delete)
    for export_obj in exports_to_delete:
        if export_obj.file_name and len(export_obj.file_name)>0:
            file_path = f'media/{export_obj.file_name}'
            if os.path.exists(file_path):
                os.remove(file_path)
        export_obj.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)


#.....
class ExportFileView(APIView):
    def get(self, request, task_id, *args, **kwargs):
        
        export = Export.objects.get(
            task_id=task_id
        )
        if export.status == 'queued' or export.status == 'in_progress':
            response = create_error_from_message('task_queued','Task not done yet. status= '+export.status)
            return JsonResponse(response, status=400)
        elif export.status == 'failed':
            response = create_error_from_message('task_failed','Export failed')
            return JsonResponse(response, status=400)
        file_name = export.file_name
        # Check the status of the Celery task
        # Task is completed
        file_path = settings.MEDIA_ROOT +'/'+ 'media/' + file_name
        try:
            document = open(file_path, 'rb')
            response = HttpResponse(FileWrapper(document), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="%s"' % file_name
            return response
        except FileNotFoundError as e:
            response = create_error_from_message('file_not_found','File not found.')
            print(response)
            return JsonResponse(response, status=400)
        except Exception as e:
            print(e)
            response = create_error_from_message('unknown','Unknown error occurred')
            return JsonResponse(response, status=400)
        finally:
            # Close the file
            document.close()
        # return Response("hi")