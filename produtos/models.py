from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome do Fornecedor")
    contato = models.CharField(max_length=100, verbose_name="Informações de Contato", blank=True, null=True)
    endereco = models.TextField(verbose_name="Endereço", blank=True, null=True)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Categoria")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")

    def __str__(self):
        return self.nome
    
    
class Produto(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome do Produto")
    codigo = models.CharField(max_length=50, unique=True, verbose_name="Código do Produto", blank=True)
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    quantidade = models.IntegerField(verbose_name="Quantidade em Estoque", default=0)
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, related_name="produtos", verbose_name="Fornecedor", blank=True, null=True)
    categorias = models.ManyToManyField(Categoria, related_name="produtos", verbose_name="Categorias")

    def __str__(self):
        return self.nome