# Generated by Django 3.2.9 on 2022-03-29 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LMS', '0025_alter_attendance_course_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_marks', models.IntegerField()),
                ('presentation_marks', models.IntegerField()),
                ('exam_marks', models.IntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LMS.course')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LMS.student')),
            ],
        ),
    ]
