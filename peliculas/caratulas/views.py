from django.shortcuts import render
from caratulas.models import Pelicula

def index(request):
    peliculas = Pelicula()
    lista_caratulas = peliculas.get_caratulas()
    context = {'lista_caratulas':lista_caratulas}
    return render(request, 'index.html', context)

