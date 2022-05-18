from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from ...models import Agency


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("file_name", type=str)

    def handle(self, *args, **kwargs):
        file_name = kwargs["file_name"]
        with open(f"{file_name}") as file:
            for row in file:
                common_name = row.lower().replace("\n", "")
                self.stdout.write(self.style.SUCCESS(f"{common_name} added"))
                Agency.objects.get_or_create(common_name=common_name)
        self.stdout.write(self.style.SUCCESS("list of objects added"))
