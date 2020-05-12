from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    age = models.PositiveSmallIntegerField()
    teaching_subjects = models.CharField(max_length=32)

    @property
    def info(self):
        return f'{self.id} {self.first_name} {self.last_name}, {str(self.age)}, {self.teaching_subjects}'


class Student(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    age = models.PositiveSmallIntegerField()

    @property
    def info(self):
        return f'{self.id} {self.first_name} {self.last_name}, {str(self.age)}'


class Group(models.Model):
    group_name = models.CharField(max_length=32)
    department = models.CharField(max_length=32)
    number_of_students = models.PositiveSmallIntegerField()

    @property
    def info(self):
        return f'{self.id} {self.group_name} {self.department}, {str(self.number_of_students)}'
