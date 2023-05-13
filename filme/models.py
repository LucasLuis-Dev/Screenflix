from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

LISTA_CATEGORIAS = (
    #(como a opção será armazenada no banco de dados, como será mostrada para o usuario)
    ("ANIME", "Anime"),
    ("ACAO", "Ação"),
    ("FICCAO", "Ficção"),
    ("TERROR", "terror"),
    ("SUSPENSE", "Suspense"),
    ("ROMANCE", "Romance"),
    ("DRAMA", "Drama"),
    ("COMEDIA", "Comédia"),
    ("FAMILIA", "Família"),
    ("GUERRA", "Guerra"),
    ("FANTASIA", "Fantasia"),
)

class Filme(models.Model):
    thumbnail = models.ImageField(upload_to = "imagens-dos-filmes")
    capaFilme = models.ImageField(upload_to= "imagens-dos-filmes", null=True)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=25, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    dataCriacao = models.DateTimeField(default=timezone.now)
    quantEpisodios = models.IntegerField(default=0)
    duracao = models.CharField(null=True, max_length=50)

    def __str__(self):
        return self.titulo
    

class Usuario(AbstractUser):
    filmesVistos = models.ManyToManyField('Filme')
