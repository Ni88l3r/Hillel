from django.http import HttpResponse

from generate_teachers.models import Teacher


def show_teachers(request):
    params = ['age', 'first_name', 'last_name']
    teachers = Teacher.objects.all()
    teachers_print = ''

    for param in params:
        value = request.GET.get(param)
        if value:
            teachers = teachers.filter(**{param: value})

    for teacher in teachers:
        teachers_print += teacher.info
    return HttpResponse(teachers_print)
