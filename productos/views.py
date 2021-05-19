from django.shortcuts  import render
from django.http       import HttpResponse 

# Create your views here.

def pagina_principal(request):
    return HttpResponse('Hola Mundo')

def nuevo(request):
    return HttpResponse('Nuevo producto')