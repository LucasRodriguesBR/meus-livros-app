# Generated by Django 4.0.2 on 2022-02-18 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meusLivrosApp', '0003_alter_livro_capa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='capa',
            field=models.ImageField(blank=True, default='capa-default.png', null=True, upload_to=''),
        ),
    ]
