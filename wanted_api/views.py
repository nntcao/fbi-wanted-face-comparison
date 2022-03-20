from django.http import HttpResponse
from django.conf import settings
from wanted_api.ml_service import compare_all_persons

# Create your views here.
def index(request):
    return HttpResponse("api dev server is working")

def photo(request, id):
    with open(f'{settings.BASE_DIR}/photos/{id}', "rb") as f:
        return HttpResponse(f.read(), content_type="image/jpeg")

# def find_doppel(request, id):
    # compare_all_persons()