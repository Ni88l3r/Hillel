from django.db import models

from teachers.models import Teacher
from students.models import Student


class Group(models.Model):
    group_name = models.CharField(max_length=32)
    department = models.CharField(max_length=32)
    number_of_students = models.PositiveSmallIntegerField()
    curator = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    headman = models.OneToOneField(Student, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.group_name} / {self.department}'

    @property
    def info(self) -> str:
        return f'{self.id} | {self.group_name} | {self.department} | ' \
               f'{str(self.curator)} | {self.headman} | {self.number_of_students}'
