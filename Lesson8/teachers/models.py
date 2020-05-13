from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    age = models.PositiveSmallIntegerField()
    teaching_subjects = models.CharField(max_length=32)

    @property
    def info(self) -> str:
        return f'{self.id} | {self.first_name} {self.last_name} | {str(self.age)} | {self.teaching_subjects}'
