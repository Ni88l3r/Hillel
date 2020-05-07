import random

from django.http import HttpResponse

from faker import Faker

from homework5.models import Student


def generate_student(request):
    fake = Faker(['en_US', 'ru_RU', 'uk_UA'])
    student = Student.objects.create(first_name=fake.first_name(),
                                     last_name=fake.last_name(), age=random.randint(18, 35))
    student.save()
    return HttpResponse(f'{student.id} {student.last_name} {student.first_name}, {student.age}')


def generate_students(request):
    count = request.GET.get('count', '10')
    if not count.isdigit() or not int(count) or int(count) > 100:
        return HttpResponse(f'<b>ERROR!</b> Count ({count}) must be integer more than 0 and less than 100!')
    fake = Faker(['en_US', 'ru_RU', 'uk_UA'])
    students_list = ''
    for _ in range(int(count)):
        student = Student.objects.create(first_name=fake.first_name(),
                                         last_name=fake.last_name(), age=random.randint(18, 35))
        student.save()
        students_list += f'{student.id} {student.last_name} {student.first_name}, {str(student.age)} </br>'
    return HttpResponse(students_list)
