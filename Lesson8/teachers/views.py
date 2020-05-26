from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from teachers.forms import ContactUSForm, CreateTeacherForm
from teachers.models import Teacher
from teachers.tasks import send_message


def create(request):
    if request.method == 'POST':
        form = CreateTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:show'))
    else:
        form = CreateTeacherForm()
    context = {
        'create_form': form,
        'action': 'Create teacher',
    }
    return render(request, 'teacher-create-edit.html', context=context)


def edit(request, pk):
    teacher = get_object_or_404(Teacher, id=pk)
    if request.method == 'POST':
        form = CreateTeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:show'))
    else:
        form = CreateTeacherForm(instance=teacher)
    context = {
        'create_form': form,
        'action': 'Edit teacher',
        'id': pk,
    }
    return render(request, 'teacher-create-edit.html', context=context)


def delete(request, pk):
    teacher = get_object_or_404(Teacher, id=pk)
    teacher.delete()
    return HttpResponseRedirect(reverse('teachers:show'))


def show(request):
    params = ['first_name', 'last_name', 'age', 'teaching_subjects']
    teachers = Teacher.objects.all()
    for param in params:
        value = request.GET.get(param)
        if value:
            teachers = teachers.filter(**{param: value})
    context = {'teachers': teachers}
    return render(request, 'teachers-show.html', context=context)


def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        form = ContactUSForm(request.POST)
        if form.is_valid():
            email_from = request.POST.get('email_from')
            title = request.POST.get('title')
            message = request.POST.get('message')
            send_message.delay(email_from, title, message)
            return render(request, 'contact-success.html')
    else:
        form = ContactUSForm()
    context = {
        'create_form': form,
        'action': 'Contact Us',
    }
    return render(request, 'contact.html', context=context)
