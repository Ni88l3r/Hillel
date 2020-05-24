from django.contrib import admin

from groups.models import Group


class GroupAdmin(admin.ModelAdmin):
    fields = ('id', 'group_name', 'department', 'number_of_students', 'curator', 'headman')
    readonly_fields = ('id',)
    list_display = ('id', 'group_name', 'department', 'number_of_students', 'curator', 'headman')

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('curator', 'headman')


admin.site.register(Group, GroupAdmin)
