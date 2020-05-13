# Generated by Django 2.2.12 on 2020-05-10 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generate_teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('age', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
