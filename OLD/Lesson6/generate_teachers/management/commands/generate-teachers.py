import random

from django.core.management.base import BaseCommand

from faker import Faker

from generate_teachers.models import Teacher


class Command(BaseCommand):
    help = 'Generate random teachers' # noqa django requires

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='?', type=int, default=100, help='The count of teachers to be created')

    def handle(self, *args, **kwargs):
        fake = Faker(['en_US', 'ru_RU', 'uk_UA'])
        count = kwargs['count']
        teachers = []
        for _ in range(count):
            teachers.append(Teacher(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                age=random.randint(20, 60),
                teaching_subjects=fake.job(),
            ))
        Teacher.objects.bulk_create(teachers)
        self.stdout.write(f'Created {count} teachers.')
