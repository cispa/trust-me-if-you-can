from django.views.decorators.http import require_POST, require_GET
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Participation

import requests
import json
import uuid


@require_GET
def index(request):
    return render(request, 'welcome.html')


@require_POST
def start(request):
    return redirect('survey', uid=str(uuid.uuid4()))


def page(request, uid):
    if Participation.objects.filter(user=uid).exists():
        messages.error(request, 'User already filled out the survey')
        return redirect('index')
    return render(request, 'survey.html', context={'uid': uid})


@require_POST
def save(request):
    data = dict()
    for k, v in dict(request.POST).items():
        if k != 'csrfmiddlewaretoken':
            data[k] = v[0]
    uid = data['uuid']
    p = Participation(user=uid)
    del data['uuid']
    p.survey = data
    p.save()
    return redirect('finish', uid=uid)


def finish(request, uid):
    values = json.dumps({"text": f"A new participant ({uid}) completed the survey!"})
    # Mattermost Hook:
    # requests.post('https://MATTERMOST.TLD/hooks/CHAT_ID', data=values)
    return render(request, 'finish.html')
