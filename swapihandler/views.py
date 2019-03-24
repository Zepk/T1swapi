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
    characters = {}
    planets = {}
    starships = {}
    for url in datos['characters']:
        reqchar = requests.get('{}'.format(url)).json()
        nombre = reqchar['name']
        url = url.split('/')
        id = url[-2]
        characters.update({nombre:id})
    for url in datos['planets']:
        reqplan = requests.get('{}'.format(url)).json()
        nombre = reqplan['name']
        url = url.split('/')
        id = url[-2]
        planets.update({nombre:id})
    for url in datos['starships']:
        reqships = requests.get('{}'.format(url)).json()
        nombre = reqships['name']
        url = url.split('/')
        id = url[-2]
        starships.update({nombre:id})
    context = {
        'movie': datos,
        'characters': characters,
        'planets': planets,
        'starships': starships,

    }
    return HttpResponse(template.render(context, request))


def character_detail(request, number):
    r = requests.get('https://swapi.co/api/people/{}'.format(number))
    datos = r.json()
