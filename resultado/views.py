from resultado.models import DadosWeb
from resultado.forms import NovoResultadoForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ResultadosListView(ListView):
    model = DadosWeb
    template_name = 'lista_resultado.html'
    context_object_name = 'resultados'

    def get_queryset(self):
        lista = super().get_queryset().order_by('data_de_atualizacao')
        search = self.request.GET.get('search')
        if search:
            lista = lista.filter(edital__icontains=search)
        
        return lista

class ResultadoDetalheView(DetailView):
    model = DadosWeb
    template_name = 'resultado_detalhe.html'

@method_decorator(login_required(login_url='login'), name='dispatch')
class ResultadoUpdateView(UpdateView):
    model = DadosWeb
    form_class = NovoResultadoForm
    template_name = 'resultado_update.html'
    success_url = '/resultados/'

@method_decorator(login_required(login_url='login'), name='dispatch')
class ResultadoDeleteView(DeleteView):
    model = DadosWeb
    template_name = 'resultado_delete.html'
    success_url = '/resultados/'

@method_decorator(login_required(login_url='login'), name='dispatch')
class NovoResultadoView(CreateView):
    model = DadosWeb
    form_class = NovoResultadoForm
    template_name = 'novo_resultado.html'
    success_url = '/resultados/'

# class NovoResultadoView(View):

#     def get(self, request):
#         novo_resultado_form = NovoResultadoForm()
#         return render(request, 'novo_resultado.html', { 'novo_resultado_form': novo_resultado_form})
    
#     def post(self, request):
#         novo_resultado_form = NovoResultadoForm(request.POST)
#         if novo_resultado_form.is_valid():
#             novo_resultado_form.save()
#             return redirect('lista_resultado')
#         return render(request, 'novo_resultado.html', { 'novo_resultado_form': novo_resultado_form})
        
