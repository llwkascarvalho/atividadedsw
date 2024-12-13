from django.contrib import admin

# Register your models here.

from produtos.models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'preco', 'quantidade', 'data_criacao')
    search_fields = ('codigo', 'nome')
    list_filter = ('data_criacao',)
    ordering = ('-data_criacao',)