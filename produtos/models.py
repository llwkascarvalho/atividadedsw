from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome do Produto")
    codigo = models.CharField(max_length=50, unique=True, verbose_name="Código do Produto")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    quantidade = models.IntegerField(verbose_name="Quantidade em Estoque")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
