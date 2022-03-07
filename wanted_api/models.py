from django.db import models

# Create your models here.
class Person(models.Model):
    title = models.CharField(max_length=100)
    front_image = models.ImageField(upload_to='photos/')
    url = models.URLField()
    reward = models.IntegerField(default=0, null=True, blank=True)
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

    def __str__(self):
        return self.title

class Aliases(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    alias = models.CharField(max_length=50)

    def __str__(self):
        return self.person.title + ': ' + self.alias