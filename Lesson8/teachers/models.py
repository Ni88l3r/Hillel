from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    age = models.PositiveSmallIntegerField()
    teaching_subjects = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def info(self) -> str:
        return f'{self.id} | {self.first_name} {self.last_name} | {str(self.age)} | {self.teaching_subjects}'


class Logger(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=16)
    path = models.CharField(max_length=64)
    execution_time = models.FloatField()

    @property
    def info(self) -> str:
        return f'{self.id} {self.created} {self.method} {self.path} {str(self.execution_time)}'
