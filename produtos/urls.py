from django.urls import path
from . import views

urlpatterns = [
    path('', views.produto_list, name='produto_list'),  # Alterar para uma URL mais simples
    path('<int:pk>/', views.produto_detail, name='produto_detail'),
    path('categorias/', views.categoria_list, name='categoria_list'),
    path('fornecedores/', views.fornecedor_list, name='fornecedor_list'),
]
