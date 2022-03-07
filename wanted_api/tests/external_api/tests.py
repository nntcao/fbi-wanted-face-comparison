from django.test import TestCase
from wanted_api.external_api_service import _get_wanted_list, update_wanted_persons
from wanted_api.models import Person

class FbiApi(TestCase):
    def setUp(self):
        update_wanted_persons()
    
    def test_get_wanted_list(self):
        wanted_list = _get_wanted_list()
        self.assertGreaterEqual(len(wanted_list), 1)

    def test_wanted_list_to_model(self):
        self.assertGreaterEqual(Person.objects.count(), 1)

    def test_get_first_person(self):
        first_person = Person.objects.get(pk=1)
        self.assertNotEqual(first_person.title, None)
        self.assertNotEqual(first_person.url, None)
            
