import random

from django.core.management.base import BaseCommand

from faker import Faker

from groups.models import Group


class Command(BaseCommand):
    help = 'Generate random groups' # noqa django requires

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='?', type=int, default=100, help='The count of groups to be created')

    def handle(self, *args, **kwargs):
        fake = Faker()
        count = kwargs['count']
        groups = []
        for _ in range(count):
            groups.append(Group(
                group_name=fake.city(),
                department=fake.job(),
                number_of_students=random.randint(20, 30),
            ))
        Group.objects.bulk_create(groups)
        self.stdout.write(f'Created {count} groups.')
