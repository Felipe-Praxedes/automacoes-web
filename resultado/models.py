from django.db import models


class DadosWeb(models.Model):
    id = models.AutoField(primary_key=True)
    objeto = models.TextField(blank=True, null=True)
    edital = models.CharField(max_length=50, blank=True, null=True)
    numero_licitacao = models.IntegerField(blank=True, null=True)
    processo = models.CharField(max_length=50, blank=True, null=True)
    edital_online = models.CharField(max_length=50, blank=True, null=True)
    datas = models.CharField(max_length=200, blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)
    unidade_licitante = models.TextField(blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    cep = models.CharField(max_length=20, blank=True, null=True)
    cidade = models.CharField(max_length=150, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    data_de_criacao = models.DateTimeField(auto_now_add=True)
    data_de_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.model
