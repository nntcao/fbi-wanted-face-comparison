from django.contrib import admin

# Register your models here.
from .models import Person, Alias


class PersonAdmin(admin.ModelAdmin):
    fields = ['title', 'front_image', 'url', 'reward', 'details', 'caution']

admin.site.register(Person, PersonAdmin)