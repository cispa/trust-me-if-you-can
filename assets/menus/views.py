from django.views.decorators.http import require_GET
from django.http import JsonResponse, HttpResponse
from django.conf import settings

import random
import os


@require_GET
def get_dishes(request):
    if request.META.get('HTTP_HOST', '').startswith('mensa.'):
        files = random.sample(os.listdir(os.path.join(settings.BASE_DIR, 'menus/dishes')), 3)
        js = [open(os.path.join(settings.BASE_DIR, 'menus/dishes', f)).read().strip() for f in files]
        response = JsonResponse(js, safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        response['Access-Control-Max-Age'] = '1728000'
        return response
    return HttpResponse(status=404)


@require_GET
def mensa(request):
    js = open(os.path.join(settings.BASE_DIR, 'menus/static/mensa.js')).read()
    response =HttpResponse(js, content_type="application/x-javascript")
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = '*'
    response['Access-Control-Allow-Headers'] = '*'
    response['Access-Control-Max-Age'] = '1728000'
    return response
