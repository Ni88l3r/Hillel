from django import forms

from generate_teachers.models import Group, Student, Teacher


class CreateTeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = ('first_name', 'last_name', 'age', 'teaching_subjects')


class CreateStudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'age')


class CreateGroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ('group_name', 'department', 'number_of_students')
