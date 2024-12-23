from django.shortcuts import render, get_object_or_404
from .models import Produto, Categoria, Fornecedor

def produto_list(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/produto_list.html', {'produtos': produtos})

def produto_detail(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'produtos/produto_detail.html', {'produto': produto})

def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'produtos/categoria_list.html', {'categorias': categorias})

def fornecedor_list(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'produtos/fornecedor_list.html', {'fornecedores': fornecedores})

def categoria_produtos(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    produtos = Produto.objects.filter(categorias=categoria)
    return render(request, 'produtos/categoria_produtos.html', {'categoria': categoria, 'produtos': produtos})

