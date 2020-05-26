from django.contrib import admin

from teachers.models import Logger, Teacher


class TeacherAdmin(admin.ModelAdmin):
    fields = ('id', 'first_name', 'last_name', 'age', 'teaching_subjects')
    readonly_fields = ('id',)
    list_display = ('id', 'first_name', 'last_name', 'age', 'teaching_subjects')


admin.site.register(Teacher, TeacherAdmin)


class LoggerAdmin(admin.ModelAdmin):
    fields = ('id', 'created', 'method', 'path', 'execution_time')
    readonly_fields = ('id', 'created', 'method', 'path', 'execution_time')
    list_display = ('id', 'created', 'method', 'path', 'execution_time')


admin.site.register(Logger, LoggerAdmin)
