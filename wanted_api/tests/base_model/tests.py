from django.test import TestCase
from wanted_api.models import Person, Aliases

# Create your tests here.

class PersonTest(TestCase):
    def setUp(self):
        test_person = Person.objects.create(
            title="test",
            url="https://www.google.com",
            reward=0,
            race="blue",
            nationality="globe",
            details="This is a test case testing the functionality of the model.",
            height_min=5,
            height_max=6,
            weight_min=3,
            weight_max=4,
            age_min=12,
            age_max=13,
            hair_color="green",
            eye_color="gray",
            description="An empty text string",
            caution="sadfhskdjfh",
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
        person = Person.objects.get(race="blue")
        self.assertEqual(person.race, "blue")
        self.assertEqual(person.height_min, 5)

    def test_get_aliases(self):
        person = Person.objects.get(race="blue")
        aliases = Aliases.objects.filter(person=person)
        self.assertEqual(aliases[0].alias, "The One")
        self.assertEqual(aliases[1].alias, "The Second")


    
