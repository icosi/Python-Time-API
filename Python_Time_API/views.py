from datetime import datetime
from django.http import HttpResponse


def time(request):
    return HttpResponse(datetime.utcnow())
