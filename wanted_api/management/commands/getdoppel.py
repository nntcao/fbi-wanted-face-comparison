from click import BaseCommand
from django.core.management.base import BaseCommand
from wanted_api.ml_service import compare_all_persons
from django.conf import settings

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("photo_path", nargs="+", type=str)

    def handle(self, *args, **options):
        for photo_path in options["photo_path"]:
            compare_all_persons(photo_path)