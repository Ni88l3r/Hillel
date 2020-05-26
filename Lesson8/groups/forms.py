from django import forms

from groups.models import Group


class CreateGroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ('group_name', 'department', 'curator', 'headman', 'number_of_students')
