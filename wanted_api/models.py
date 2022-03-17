from django.core.files.base import ContentFile
from django.db import models
from wanted_api.external_api_service import get_image
import time


# Create your models here.
class Person(models.Model):
    title = models.CharField(max_length=100)
    front_image = models.ImageField(upload_to='./photos/')
    url = models.URLField()
    reward = models.TextField(null=True, blank=True)
    race = models.CharField(max_length=50, null=True, blank=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    height_min = models.IntegerField(default=0, null=True, blank=True)
    height_max = models.IntegerField(default=0, null=True, blank=True)
    weight_min = models.IntegerField(default=0, null=True, blank=True)
    weight_max = models.IntegerField(default=0, null=True, blank=True)
    age_min = models.IntegerField(default=0, null=True, blank=True)
    age_max = models.IntegerField(default=0, null=True, blank=True)
    hair_color = models.CharField(max_length=50, null=True, blank=True)
    eye_color = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    caution = models.TextField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    @classmethod
    def create_from_json(cls, json):
        if not cls.is_valid_json(json):
            return None

        person, success = cls.objects.update_or_create(
            title = json["title"],
            defaults={
                "url": json["url"],
                "reward": json["reward_text"],
                "race": json["race"],
                "nationality": json["nationality"],
                "details": json["details"],
                "height_min": json["height_min"],
                "height_max": json["height_max"],
                "weight_min": json["weight_min"],
                "age_min": json["age_min"],
                "age_max": json["age_max"],
                "hair_color": json["hair_raw"],
                "eye_color": json["eyes_raw"],
                "description": json["description"],
                "caution": json["caution"],
                "remarks": json["remarks"]
            }
        )
        if json["aliases"]:
            for data in json["aliases"]:
                Alias.create_from_json(data, person)

        if not person.front_image:
            time.sleep(0.01)

            image_url = json["images"][0]["original"]
            image_name, image_content = get_image(image_url)
            person.front_image.save(image_name, ContentFile(image_content))
        person.save()
        return person

    @classmethod
    def is_valid_json(cls, json):
        url = json["url"]
        return not ("missing-persons" in url \
                or "seeking-info" in url \
                or "kidnap" in url \
                or "victim" in url \
                or "unidentified" in url \
                or "unknown" in url) \


class Alias(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    alias = models.CharField(max_length=50)

    def __str__(self):
        return self.person.title + ': ' + self.alias

    @classmethod
    def create_from_json(cls, json, person):
        alias, success = cls.objects.update_or_create(
            person = person,
            alias = json
        )
        if not success: 
            return None
        alias.save()
        return alias
