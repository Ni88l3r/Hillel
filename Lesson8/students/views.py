from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from students.forms import CreateStudentForm
from students.models import Student


def create(request):
    if request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:show'))
    else:
        form = CreateStudentForm()
    context = {
        'create_form': form,
        'action': 'Create student',
    }
    return render(request, 'student-create-edit.html', context=context)


def edit(request, pk):
    student = get_object_or_404(Student, id=pk)
    if request.method == 'POST':
        form = CreateStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:show'))
    else:
        form = CreateStudentForm(instance=student)
    context = {
        'create_form': form,
        'action': 'Create student',
        'id': pk,
    }
    return render(request, 'student-create-edit.html', context=context)


def delete(request, pk):
    student = get_object_or_404(Student, id=pk)
    student.delete()
    return HttpResponseRedirect(reverse('students:show'))


def show(request):
    params = ['age', 'first_name', 'last_name']
    students = Student.objects.all()
    for param in params:
        value = request.GET.get(param)
        if value:
            students = students.filter(**{param: value})
    context = {'students': students}
    return render(request, 'students-show.html', context=context)
