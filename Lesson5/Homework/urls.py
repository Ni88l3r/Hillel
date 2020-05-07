"""Homework URL Configuration

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

from group.views import show_groups

from homework5.views import generate_student, generate_students

from teachers.views import show_teachers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate-student/', generate_student, name='generate_student'),
    path('generate-students/', generate_students, name='generate_students'),
    path('teachers/', show_teachers, name='teachers'),
    path('groups/', show_groups, name='groups'),
]
