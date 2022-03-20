from django.core.management.base import BaseCommand
from wanted_api.external_api_service import get_wanted_list
from wanted_api.models import Person

class Command(BaseCommand):
    def handle(self, *args, **options):
        wanted_list = get_wanted_list()
        persons = [Person.create_from_json(json) for json in wanted_list]
        # filtered_persons = list(filter(None, persons))
        # for person in filtered_persons:
        #     print(person)
