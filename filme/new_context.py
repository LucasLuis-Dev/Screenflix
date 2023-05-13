from .models import Filme


def listaFilmesRecentes(request):
    listaFilmes = Filme.objects.all().order_by('-dataCriacao')[0:12]
    if listaFilmes:
        return {"filmesRecentes" : listaFilmes}
    
    else:
        listaFilmes = None
        return {"filmesRecentes" : listaFilmes}


def listaFilmesPopulares(request):
    listaFilmes = Filme.objects.all().order_by('-visualizacoes')[0:8]
    if listaFilmes:
        return {"filmesPopulares" : listaFilmes}
    
    else:
        listaFilmes = None
        return {"filmesPopulares" : listaFilmes}
    

def filmeMaisAssistido(request):
    listaFilmes = Filme.objects.all().order_by('-visualizacoes')[0]
    if listaFilmes:
        return {"filmeMaisAssistido" : listaFilmes}
    
    else:
        listaFilmes = None
        return {"filmeMaisAssistido" : listaFilmes}
    


def listaAnimes(request):
    listaAnimes = Filme.objects.filter(categoria__icontains='ANIME')
    return {'animes': listaAnimes}