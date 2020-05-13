from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    age = models.PositiveSmallIntegerField()
    teaching_subjects = models.CharField(max_length=32)

    @property
    def info(self):
        return f'{self.id} {self.last_name} {self.first_name}, {str(self.age)}, ' \
                         f'{self.teaching_subjects} </br>'
