from django.urls import path

from students import views

app_name = "students"

urlpatterns = [
    path('create/', views.create, name='create'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('show/', views.show, name='show'),
]
