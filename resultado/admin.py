from django.contrib import admin
from resultado.models import DadosWeb

class ResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'objeto', 'edital', 'numero_licitacao', 'processo', 'edital_online', 'datas', 'observacao', 'unidade_licitante', 
                    'endereco', 'cep', 'cidade' , 'descricao', 'data_de_criacao', 'data_de_atualizacao']

    search_fields = ['objeto', 'edital', 'numero_licitacao', 'processo', 'data_de_criacao', 'data_de_atualizacao']

admin.site.register(DadosWeb, ResultAdmin)