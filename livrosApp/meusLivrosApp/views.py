from django.shortcuts import render, redirect
from .models import Livro
from .forms import AdicionarLivroForm


# Create your views here.

# Lista todos os livros cadastrados


def livros(request):
    num_livro = 1
    livros = Livro.objects.all()
    contexto = {'livros': livros, 'numeracao': num_livro}
    return render(request, 'meusLivrosApp/index.html', contexto)


def adicionarLivro(request):
    form = AdicionarLivroForm()
    if request.method == 'POST':

        form = AdicionarLivroForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('livros')

    contexto = {'form': form}
    return render(request, 'meusLivrosApp/livro_form.html', contexto)


def editarLivro(request, livro_id):
    livro_selecionado = Livro.objects.get(id=livro_id)
    form = AdicionarLivroForm(instance=livro_selecionado)

    if request.method == 'POST':
        form = AdicionarLivroForm(request.POST, request.FILES, instance=livro_selecionado)
        if form.is_valid():
            form.save()
        return redirect('livros')

    contexto = {'form': form}
    cont = 2
    return render(request, 'meusLivrosApp/livro_form.html', contexto)


def deletarLivro(request, livro_id):
    livro_selecionado = Livro.objects.get(id=livro_id)

    if request.method == 'POST':
        livro_selecionado.delete()
        return redirect('livros')

    return render(request, 'meusLivrosApp/conf_deletar.html', {'livro': livro_selecionado})
