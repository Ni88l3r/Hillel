from django.urls import path

from generate_teachers import views

app_name = "generate_teachers"

urlpatterns = [
    path('create-teacher/', views.create_teacher, name='create-teacher'),
    path('create-student/', views.create_student, name='create-student'),
    path('create-group/', views.create_group, name='create-group'),
    path('teachers/', views.show_teachers, name='teachers'),
    path('students/', views.show_students, name='students'),
    path('groups/', views.show_groups, name='groups'),
]
