from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    age = models.PositiveSmallIntegerField()
    phone = models.CharField(max_length=16, default='')

    @property
    def info(self) -> str:
        return f'{self.id} | {self.first_name} {self.last_name} | {str(self.age)} | {self.phone}'
