import random

from django.core.management.base import BaseCommand

from faker import Faker

from students.models import Student


class Command(BaseCommand):
    help = 'Generate random students' # noqa django requires

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='?', type=int, default=100, help='The count of students to be created')

    def handle(self, *args, **kwargs):
        fake = Faker()
        count = kwargs['count']
        students = []
        for _ in range(count):
            students.append(Student(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                age=random.randint(20, 60),
            ))
        Student.objects.bulk_create(students)
        self.stdout.write(f'Created {count} students.')
