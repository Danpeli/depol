from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('App de registro de Boletins de Ocorrência e de registros de diário de serviço com passagem de turno')