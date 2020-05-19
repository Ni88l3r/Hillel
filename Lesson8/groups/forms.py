from django import forms

from groups.models import Group


class CreateGroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ('group_name', 'department', 'number_of_students')
