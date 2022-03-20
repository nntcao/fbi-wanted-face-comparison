import cv2
from deepface import DeepFace
from wanted_api.models import Person
from django.conf import settings


def compare_all_persons(img_path):
    img1_p = f"{settings.BASE_DIR}/{img_path}"
    min_person = None
    min_distance = 1
    for person in Person.objects.all():
        img2_p = f"{settings.BASE_DIR}/{person.front_image}"

        # img1 = cv2.imread(img1_p)
        # img2 = cv2.imread(img2_p)

        result = DeepFace.verify(img1_path=img1_p, img2_path=img2_p, distance_metric="cosine", enforce_detection=False)
        if result["distance"] < min_distance:
            min_distance = result["distance"]
            min_person = person
    print(min_distance)
    print(min_person)
    return min_person


