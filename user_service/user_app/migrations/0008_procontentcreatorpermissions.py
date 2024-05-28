# Generated by Django 4.0.10 on 2024-02-12 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0007_delete_procontentcreatorpermissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProContentCreatorPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('create_movie', 'Create Movie'), ('update_movie', 'Update own movie'), ('delete_movie', 'Delete own movie'), ('read_all_my_movies', 'Read all own movies')),
                'managed': False,
                'default_permissions': (),
            },
        ),
    ]