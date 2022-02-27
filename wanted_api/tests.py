from ast import alias
from re import M
from turtle import title
from django.test import TestCase
from wanted_api.models import Person, Aliases

# Create your tests here.


class PeopleTestCase(TestCase):
    def setUp(self):
        test_person = Person.objects.create(title="test",
            url="https://www.zenonscraper.com",
            reward=0,
            race="blue",
            nationality="globe",
            details="This is a test case testing the functionality of the model.",
            height=5,
            weight=3,
            age=12,
            hair_color="green",
            eye_color="gray",
            description="An empty text string"
        )
        test_person.save()
        
        test_alias1 = Aliases.objects.create(
            person=test_person,
            alias="The One"
        )
        test_alias2 = Aliases.objects.create(
            person=test_person,
            alias="The Second"
        )

        test_alias1.save()
        test_alias2.save()

    def test_get_person(self):
        self.assertEqual(person.race, "blue")
        self.assertEqual(person.height, 5)

    def test_get_aliases(self):
        person = Person.objects.get(race="blue")
        aliases = Aliases(person=person)
        self.assertEqual(aliases[0], "The One")
        self.assertEqual(aliases[1], "The Second")


