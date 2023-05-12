from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def landing(request): # Primera vista 

    context = {
            'title': 'HRV Endurance',
        }
    return render(request, 'landing.html')