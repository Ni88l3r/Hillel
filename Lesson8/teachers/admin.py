from django.contrib import admin

from teachers.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    fields = ('id', 'first_name', 'last_name', 'age', 'teaching_subjects')
    readonly_fields = ('id',)
    list_display = ('id', 'first_name', 'last_name', 'age', 'teaching_subjects')


admin.site.register(Teacher, TeacherAdmin)
