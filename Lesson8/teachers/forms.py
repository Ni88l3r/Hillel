from django import forms

from teachers.models import Teacher


class CreateTeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = ('first_name', 'last_name', 'age', 'teaching_subjects')


class ContactUSForm(forms.Form):
    email_from = forms.EmailField(label='From (e-mail)')
    title = forms.CharField(label='Title', max_length=100)
    message = forms.CharField(label='Message', max_length=1000, widget=forms.Textarea)
