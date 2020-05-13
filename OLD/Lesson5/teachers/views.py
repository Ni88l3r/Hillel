from django.http import HttpResponse

from teachers.models import Teacher


def show_teachers(request):
    teachers_print = ''
    teachers = Teacher.objects.all()
    for teacher in teachers:
        teachers_print += teacher.info
    return HttpResponse(teachers_print)
