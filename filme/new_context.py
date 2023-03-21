from .models import Filme


def listaFilmesRecentes(request):
    listaFilmes = Filme.objects.all().order_by('-dataCriacao')[0:12]
    return {"filmesRecentes" : listaFilmes}


def listaFilmesPopulares(request):
    listaFilmes = Filme.objects.all().order_by('-visualizacoes')[0:8]
    return {"filmesPopulares" : listaFilmes}

def filmeMaisAssistido(request):
    listaFilmes = Filme.objects.all().order_by('-visualizacoes')[0]
    return {"filmeMaisAssistido" : listaFilmes}