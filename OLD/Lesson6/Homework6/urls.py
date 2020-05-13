from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from generate_teachers import views


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('generate_teachers/', include('generate_teachers.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
