from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

# Create your views here.
def index(request):
    return HttpResponse("api dev server is working")

def photo(request, id):
    with open(f'{settings.BASE_DIR}/photos/{id}', "rb") as f:
        return HttpResponse(f.read(), content_type="image/jpeg")