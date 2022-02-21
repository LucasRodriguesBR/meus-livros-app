from django.forms import ModelForm
from .models import Livro
from django import forms


class AdicionarLivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = ['nome', 'autor', 'resenha', 'data']

    def __init__(self, *args, **kwargs):
        super(AdicionarLivroForm, self).__init__(*args, **kwargs)
        self.fields['nome'].label = 'Título'
        self.fields['data'].label = 'Mês de leitura'

        self.fields['data'].widget.attrs.update({'placeholder': 'Qual mês do ano você leu esse livro?'})
        self.fields['nome'].widget.attrs.update({'placeholder': 'Qual o título do livro?'})
        self.fields['autor'].widget.attrs.update({'placeholder': 'Qual o nome do autor do livro'})
        self.fields['resenha'].widget.attrs.update({'placeholder': 'O que você achou do livro? (Opcional) '})

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})





