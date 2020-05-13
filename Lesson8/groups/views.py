from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from groups.forms import CreateGroupForm
from groups.models import Group


def create(request):
    if request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:show'))
    else:
        form = CreateGroupForm()
    context = {
        'create_form': form,
        'action': 'Create group',
    }
    return render(request, 'group-create-edit.html', context=context)


def edit(request, pk):
    group = get_object_or_404(Group, id=pk)
    if request.method == 'POST':
        form = CreateGroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:show'))
    else:
        form = CreateGroupForm(instance=group)
    context = {
        'create_form': form,
        'action': 'Edit group',
        'id': pk,
    }
    return render(request, 'group-create-edit.html', context=context)


def delete(request, pk):
    group = get_object_or_404(Group, id=pk)
    group.delete()
    return HttpResponseRedirect(reverse('groups:show'))


def show(request):
    params = ['group_name', 'department', 'number_of_students']
    groups = Group.objects.all()
    for param in params:
        value = request.GET.get(param)
        if value:
            groups = groups.filter(**{param: value})
    context = {'groups': groups}
    return render(request, 'groups-show.html', context=context)
