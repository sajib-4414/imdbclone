# Generated by Django 4.2.5 on 2023-12-16 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_alter_movie_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streamplatform',
            name='about',
            field=models.TextField(),
        ),
    ]
