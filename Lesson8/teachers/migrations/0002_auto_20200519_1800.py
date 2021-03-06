# Generated by Django 2.2.12 on 2020-05-19 15:00

from django.db import migrations


def forwards(apps, schema):
    Teacher = apps.get_model('teachers', 'Teacher')
    for teacher in Teacher.objects.all().only('first_name', 'last_name').iterator():
        teacher.first_name = str.capitalize(teacher.first_name)
        teacher.last_name = str.capitalize(teacher.last_name)
        teacher.save(update_fields=['first_name', 'last_name'])


def backwards(apps, schema):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
