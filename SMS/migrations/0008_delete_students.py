# Generated by Django 3.2.9 on 2022-03-21 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SMS', '0007_course_session_year'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Students',
        ),
    ]