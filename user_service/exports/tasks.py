# tasks.py
from celery import shared_task
from time import sleep
from django.core.files.storage import default_storage
import pandas as pd
from exports.models import Export
from io import BytesIO
import datetime
from django.contrib.auth import get_user_model
User = get_user_model()

@shared_task
def add():
    sleep(5)  # Simulating a time-consuming task
    print(" I am printing from worker.......")
    return "retrurn value from worker...."

@shared_task
def generate_csv_file(userid):
    try:
        user = User.objects.get(id=userid)
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
        export = Export.objects.get(
            task_id=generate_csv_file.request.id
        )
        export.file_name = output_file_name
        export.status = Export.STATUS_CHOICES[2][0]
        export.save()
        return file_path
    except Exception as e:
        export = Export.objects.get(
            task_id=generate_csv_file.request.id
        )
        export.file_name = output_file_name
        export.status = Export.STATUS_CHOICES[3][0] #failed
        export.save()
        return "Exception occurred in export creation"