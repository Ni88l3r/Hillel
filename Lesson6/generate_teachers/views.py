from django.http import HttpResponseRedirect
from django.shortcuts import render

from generate_teachers.forms import CreateGroupForm, CreateStudentForm, CreateTeacherForm
from generate_teachers.models import Group, Student, Teacher


def create_teacher(request):
    if request.method == 'POST':
        form = CreateTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = CreateTeacherForm()
    context = {'create_form': form}
    return render(request, 'create-teacher.html', context=context)


def create_student(request):
    if request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = CreateStudentForm()
    context = {'create_form': form}
    return render(request, 'create-student.html', context=context)


def create_group(request):
    if request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = CreateGroupForm()
    context = {'create_form': form}
    return render(request, 'create-group.html', context=context)


def show_teachers(request):
    params = ['first_name', 'last_name', 'age', 'teaching_subjects']
    teachers = Teacher.objects.all()
    for param in params:
        value = request.GET.get(param)
        if value:
            teachers = teachers.filter(**{param: value})
    context = {'teachers': teachers}
    return render(request, 'show-teachers.html', context=context)


def show_students(request):
    params = ['age', 'first_name', 'last_name']
    students = Student.objects.all()
    for param in params:
        value = request.GET.get(param)
        if value:
            students = students.filter(**{param: value})
    context = {'students': students}
    return render(request, 'show-students.html', context=context)


def show_groups(request):
    params = ['group_name', 'department', 'number_of_students']
    groups = Group.objects.all()
    for param in params:
        value = request.GET.get(param)
        if value:
            groups = groups.filter(**{param: value})
    context = {'groups': groups}
    return render(request, 'show-groups.html', context=context)


def index(request):
    return render(request, 'index.html')
