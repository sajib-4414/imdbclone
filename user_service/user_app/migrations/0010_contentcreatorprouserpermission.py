# Generated by Django 4.0.10 on 2024-02-12 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('user_app', '0009_regularprouserpermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentCreatorProUserPermission',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.permission',),
        ),
    ]