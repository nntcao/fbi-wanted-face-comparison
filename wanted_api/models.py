from tkinter import CASCADE
from django.db import models
from pyparsing import empty

# Create your models here.
class Person(models.Model):
    title = models.CharField(max_length=50)
    front_image = models.ImageField(upload_to='photos/')
    url = models.URLField()
    reward = models.IntegerField(default=0, blank=True)
    race = models.CharField(max_length=50, blank=True)
    nationality = models.CharField(max_length=50, blank=True)
    details = models.TextField(blank=True)
    height = models.IntegerField(blank=True)
    weight = models.IntegerField(blank=True)
    age = models.IntegerField(blank=True)
    hair_color = models.CharField(blank=True)
    eye_color = models.CharField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Aliases(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    alias = models.CharField(max_length=50)

    def __str__(self):
        return self.person.title + ': ' + self.alias