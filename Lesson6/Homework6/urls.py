"""Homework6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from generate_teachers.views import create_group, create_student, create_teacher, index, \
                                    show_groups, show_students, show_teachers


urlpatterns = [
    path('', index, name='index'),
    path('create-teacher/', create_teacher, name='create-teacher'),
    path('create-student/', create_student, name='create-student'),
    path('create-group/', create_group, name='create-group'),
    path('admin/', admin.site.urls),
    path('teachers/', show_teachers, name='teachers'),
    path('students/', show_students, name='students'),
    path('groups/', show_groups, name='groups'),
]
