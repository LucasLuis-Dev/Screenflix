from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView
# Create your views here.

class Homepage(TemplateView):
    template_name = 'homepage.html'
 

class Homeconteudo(ListView):
    template_name = "homeconteudo.html"
    model = Filme
    # Object_list


class DetalhesConteudo(DetailView):
    template_name = 'detalhesConteudo.html'
    model = Filme
    # Object -> 1 item do nosso modelo

    def get_context_data(self, **kwargs):
        context = super(DetalhesConteudo, self).get_context_data(**kwargs)

        filmesRelacionados = Filme.objects.filter(categoria=self.get_object().categoria)
        context['filmesRelacionados'] = filmesRelacionados

        return context
