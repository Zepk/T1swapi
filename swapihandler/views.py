from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
import json


def index(request):
    r = requests.get('https://swapi.co/api/films')
    datos = r.json()
    template = loader.get_template('swapihandler/index.html')
    id = 0
    for i in datos['results']:
        id += 1
        req = requests.get('https://swapi.co/api/films/{}'.format(id))
        req = req.json()
        for j in datos['results']:
            if j["episode_id"] == req["episode_id"]:
                j.update({'id':id})
                


    context = {
        'datos': datos,
    }
    return HttpResponse(template.render(context, request))

def movie_detail(request, number):
    r = requests.get('https://swapi.co/api/films/{}'.format(number))
    datos = r.json()
    template = loader.get_template('swapihandler/moviedetail.html')
    context = {
        'movie': datos,
    }
    return HttpResponse(template.render(context, request))
