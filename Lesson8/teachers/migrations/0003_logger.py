# Generated by Django 2.2.12 on 2020-05-20 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_auto_20200519_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('method', models.CharField(max_length=16)),
                ('path', models.CharField(max_length=64)),
                ('execution_time', models.FloatField()),
            ],
        ),
    ]
