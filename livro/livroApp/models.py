from django.db import models

# Create your models here.
class Livro(models.Model):
    nome_livro = models.CharField(max_length=30)
    autor_livro = models.CharField(max_length=30)
    ano_publicacao = models.IntegerField()
    nota_livro = models.FloatField(blank=True, null=True)
    obs_livro = models.TextField(blank=True, null=True)
    data_inicio = models.DateField(blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)
