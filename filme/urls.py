from django.urls import path, reverse_lazy
from .views import Homepage, Homeconteudo, DetalhesConteudo, Pesquisar, PaginaPerfil, CriarConta,CustomLoginView
from django.contrib.auth import views as auth_view

app_name = 'filme' 

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'), 
    path('conteudos/', Homeconteudo.as_view(), name='homeconteudo'), 
    path('conteudos/<int:pk>', DetalhesConteudo.as_view(), name='detalhesconteudo'),
    path('pesquisa/', Pesquisar.as_view(), name='pesquisaConteudo'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='homepage.html', next_page='/'), name='logout'),
    path('perfil/<int:pk>', PaginaPerfil.as_view(), name='perfil'),
    path('criarConta/', CriarConta.as_view(), name='criarconta'),
    path('mudarsenha/', auth_view.PasswordChangeView.as_view(template_name='mudarSenha.html', success_url=reverse_lazy('filme:homeconteudos')), name='mudarsenha'),
]
