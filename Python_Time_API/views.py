from datetime import datetime
from django.http import JsonResponse


def time(request):
    return JsonResponse({"time": datetime.utcnow()})
