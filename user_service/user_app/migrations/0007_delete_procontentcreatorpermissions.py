# Generated by Django 4.0.10 on 2024-02-12 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0006_alter_procontentcreatorpermissions_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProContentCreatorPermissions',
        ),
    ]