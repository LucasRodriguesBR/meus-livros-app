# Generated by Django 4.0.2 on 2022-02-19 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meusLivrosApp', '0005_livro_autor_alter_livro_capa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livro',
            old_name='descricao',
            new_name='resenha',
        ),
    ]
