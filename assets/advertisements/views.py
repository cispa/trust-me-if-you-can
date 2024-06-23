from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.http import require_GET
from django.conf import settings

import random
import os


@require_GET
def get_random_ad(request):
    if request.META.get('HTTP_HOST', '').startswith('ads.'):
        ad = random.choice(os.listdir(os.path.join(settings.BASE_DIR, 'advertisements/ads')))
        return HttpResponseRedirect(f'http://{ad.replace(".js", "")}-{request.META.get("HTTP_HOST", "")}/')
    return HttpResponse(status=404)


@require_GET
def load_ad(request):
    host = request.META.get('HTTP_HOST', '')
    if '-ads.' in host:
        ad_name = os.path.basename(host.split('-ads')[0])
        ad_path = os.path.join(settings.BASE_DIR, 'advertisements/ads', ad_name + '.js')
        return HttpResponse(open(ad_path, 'r').read(), content_type="application/x-javascript")
    return HttpResponse(status=404)