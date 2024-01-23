from django.contrib import admin
from django.urls import path
from accounts.views import register_view, gerenciar_user_view, login_view, logout_view
from resultado.views import ResultadosListView, NovoResultadoView, ResultadoDetalheView, ResultadoUpdateView, ResultadoDeleteView

urlpatterns = [
    path('', ResultadosListView.as_view(), name ='Pagina_inicial'),
    path('admin/', admin.site.urls),
    path('login/', login_view, name ='login'),
    path('gerenciar_user/', gerenciar_user_view, name ='gerenciar_user'),
    path('logout/', logout_view, name ='logout'),
    path('registrar/', register_view, name ='registro'),
    path('resultados/', ResultadosListView.as_view(), name ='lista_resultado'),
    path('novo_resultado/', NovoResultadoView.as_view(), name ='novo_resultado'),
    path('resultado/<int:pk>', ResultadoDetalheView.as_view(), name ='resultado_detalhe'),
    path('resultado/<int:pk>/update', ResultadoUpdateView.as_view(), name ='resultado_update'),
    path('resultado/<int:pk>/delete', ResultadoDeleteView.as_view(), name ='resultado_delete')
]
