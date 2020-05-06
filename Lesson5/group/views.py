from django.http import HttpResponse

from group.models import Group


def show_groups(request):
    groups_print = ''
    groups = Group.objects.all()
    for group in groups:
        groups_print += group.info
    return HttpResponse(groups_print)
