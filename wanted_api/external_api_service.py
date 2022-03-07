import requests
from wanted_api.models import Aliases, Person

def _get_wanted_list():
    base_url = "https://api.fbi.gov/wanted/v1/list"
    wanted_list = []
    for page in range(1, 2):
        response = requests.get(base_url + "?page=" + str(page)).json()
        if "items" in response:
            wanted_list.extend(response["items"])
        else:
            break
    return wanted_list

def _wanted_list_to_model(wanted_list):
    for person in wanted_list:
        person_entry, person_has_created = Person.objects.update_or_create(
            title = person["title"],
            # front_image = ,
            url = person["url"],
            reward = person["reward_max"],
            race = person["race"],
            nationality = person["nationality"],
            details = person["details"],
            height_min = person["height_min"],
            height_max = person["height_max"],
            weight_min = person["weight_min"],
            age_min = person["age_min"],
            age_max = person["age_max"],
            hair_color = person["hair_raw"],
            eye_color = person["eyes_raw"],
            description = person["description"],
            caution = person["caution"]
        )
        person_entry.save()
        aliases = person["aliases"]
        if aliases:
            for alias_person in aliases:
                alias_entry, alias_has_created = Aliases.objects.update_or_create(
                    person = person_entry,
                    alias = alias_person
                )
                alias_entry.save()

def update_wanted_persons():
    wanted_list = _get_wanted_list()
    _wanted_list_to_model(wanted_list)