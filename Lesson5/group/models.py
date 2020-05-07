from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=32)
    number_of_students = models.PositiveSmallIntegerField()

    @property
    def info(self):
        return f'{self.id} {self.group_name} : {self.number_of_students} </br>'
