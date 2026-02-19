from django.http import HttpResponse
from django.shortcuts import render
from datetime import date


# Create your views here.

def index(request):
    return HttpResponse("Hello world!\n")

def calculaEdad(request, edad, ano):
    ano_actual = date.today()
    diff_date = ano - (ano_actual.year - edad)
    return HttpResponse(diff_date)
