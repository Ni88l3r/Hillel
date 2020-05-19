# Generated by Django 2.2.12 on 2020-05-12 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=32)),
                ('department', models.CharField(max_length=32)),
                ('number_of_students', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
