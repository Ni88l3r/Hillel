from django.contrib import admin

from groups.models import Group


class GroupAdmin(admin.ModelAdmin):
    fields = ('id', 'group_name', 'department', 'number_of_students')
    readonly_fields = ('id',)
    list_display = ('id', 'group_name', 'department', 'number_of_students')


admin.site.register(Group, GroupAdmin)
