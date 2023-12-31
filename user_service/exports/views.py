from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
User = get_user_model()
import pandas as pd
from django.http import HttpResponseBadRequest,JsonResponse
from io import BytesIO
from django.core.files.storage import default_storage
import datetime
from exports.models import Export
from django.conf import settings
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from user_app.helpers.serializer_error_parser import create_error_from_message
# Create your views here.
class ExportCreateAPIView(APIView):
    permission_classes= [IsAuthenticated]
    def post(self, request, format=None):
        """
        Return a list of all users......
        """
        user = request.user
        username = user.username
        registration_time = user.date_joined
        last_login_time = user.last_login
        # Create a DataFrame
        data = {'Username': [username],
                'Registration Time': [registration_time],
                'Last Login Time': [last_login_time]}

        
        df = pd.DataFrame(data)
        df['Registration Time'] = df['Registration Time'].apply(lambda a: pd.to_datetime(a).date()) 
        df['Last Login Time'] = df['Last Login Time'].apply(lambda a: pd.to_datetime(a).date()) 
        
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1', index=False)
        writer.close()

        output.seek(0)
        # workbook = output.getvalue()
        output_name = f"export_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        output_file_name = output_name+".xlsx"
        
        file_path = f'media/{output_name}.xlsx'  # Adjust the storage path as needed
        default_storage.save(file_path, output)
        export = Export.objects.create(
            creator=user,
            file_name=output_file_name,
            status=Export.STATUS_CHOICES[0][0],
            description="Registration data, Review Data"
        )
        
        # Return a JSON response with the status and download link
        response_data = {
            'status': 'completed',
            'filename': output_file_name,
        }
        return JsonResponse(response_data, status=200)

class ExportFileView(APIView):
    def get(self, request, file_name, *args, **kwargs):
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