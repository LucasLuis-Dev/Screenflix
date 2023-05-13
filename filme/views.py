from django import forms
from django.http import HttpResponse
from .models import Filme, Usuario
from django.shortcuts import redirect,reverse
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from itertools import chain
from django.contrib.auth.views import LoginView, PasswordChangeView
from .forms import CustomLoginForm, SignUpForm, FormHomepage
# Create your views here.

class Homepage(FormView):
    template_name = 'homepage.html'
    form_class = FormHomepage

    def get_success_url(self):
        email = self.request.POST.get('email')
        usuario = Usuario.objects.filter(email=email)
        if usuario:
            return reverse('filme:login')

        else:
            return reverse('filme:criarconta')


class Homeconteudo(LoginRequiredMixin, ListView):
    template_name = "homeconteudo.html"
    model = Filme
    # Object_list


class DetalhesConteudo(LoginRequiredMixin, DetailView):
    template_name = 'detalhesConteudo.html'
    model = Filme
    # Object -> 1 item do nosso modelo

    def get(self, request, *args, **kwargs):
        
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        usuario =request.user
        usuario.filmesVistos.add(filme)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DetalhesConteudo, self).get_context_data(**kwargs)

        filmesRelacionados = Filme.objects.filter(categoria=self.get_object().categoria)
        context['filmesRelacionados'] = filmesRelacionados

        return context
    

class Pesquisar(LoginRequiredMixin, ListView):
    template_name = 'pesquisa.html'
    model = Filme

    def get_queryset(self):
        termoPesquisa = self.request.GET.get('query')
        if termoPesquisa:
            object_list = self.model.objects.filter(titulo__icontains=termoPesquisa)
            
            for filme in object_list:

                categoria = filme.categoria

            filmesParecidos = self.model.objects.filter(categoria__icontains=categoria).exclude(id=filme.id)

            object_list = list(chain(object_list, filmesParecidos))
       
            return object_list
        
        else:
            return None


class PaginaPerfil(LoginRequiredMixin, UpdateView):
    template_name = 'perfil.html'
    model = Usuario
    fields = ['username','email']
    widgets = {
            'email': forms.EmailInput(attrs={'class': 'w-[400px]'}),
        }

    def get_success_url(self):
        return reverse('filme:homeconteudos')

class MudarSenha(LoginRequiredMixin, PasswordChangeView):
    template_name = 'mudarSenha.html'

    def get_success_url(self):
        # Redireciona o usuário para a página inicial após a alteração de senha
        return reverse('filme:homeconteudos')


class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = CustomLoginForm


class CriarConta(FormView):
    template_name = 'criarConta.html'
    form_class = SignUpForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):

        return reverse('filme:login')