from django.db.models.signals import pre_save
from django.dispatch import receiver

from students.models import Student


@receiver(pre_save, sender=Student)
def student_pre_save(sender, instance, **kwargs):
    instance.first_name = str.capitalize(instance.first_name)
    instance.last_name = str.capitalize(instance.last_name)
