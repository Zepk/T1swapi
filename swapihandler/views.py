from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
import json


def index(request):
    r = requests.get('https://swapi.co/api/films')
    datos = r.json()
    template = loader.get_template('swapihandler/index.html')
    context = {
        'datos': datos,
    }
    return HttpResponse(template.render(context, request))
