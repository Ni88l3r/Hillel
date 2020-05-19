from django.contrib import admin

from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    fields = ('id', 'first_name', 'last_name', 'age')
    readonly_fields = ('id',)
    list_display = ('id', 'first_name', 'last_name', 'age')


admin.site.register(Student, StudentAdmin)
