from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.livros, name='livros'),
    path('adicionar-livro', views.adicionarLivro, name='adicionar-livro'),
    path('editar-livro/<str:livro_id>', views.editarLivro, name='editar-livro'),
    path('deletar-livro/<str:livro_id>', views.deletarLivro, name='deletar-livro'),
]