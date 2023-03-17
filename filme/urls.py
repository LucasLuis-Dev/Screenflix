from django.urls import path, include
from .views import Homepage, Homeconteudo, DetalhesConteudo

app_name = 'filme' 

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'), 
    path('conteudos/', Homeconteudo.as_view(), name='homeconteudo'), 
    path('conteudos/<int:pk>', DetalhesConteudo.as_view(), name='detalhesconteudo')
]
