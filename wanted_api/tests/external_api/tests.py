from django.test import TestCase
from wanted_api.external_api_service import get_wanted_list

class FbiApi(TestCase):
    def test_get_wanted_list(self):
        wanted_list = get_wanted_list()
        self.assertGreaterEqual(len(wanted_list), 1)
