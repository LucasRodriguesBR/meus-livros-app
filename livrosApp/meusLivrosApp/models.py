from django.db import models
import uuid
# Create your models here.


class Livro(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=False)
    autor = models.CharField(max_length=200, blank=True, null=True)
    resenha = models.TextField(null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    capa = models.ImageField(null=True, blank=True, upload_to='imagens', default='capa-default.png')
    editora = models.CharField(max_length=200, null=True, blank=True)
    ano = models.CharField(max_length=5, null=True, blank=True)
    criado = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.nome
