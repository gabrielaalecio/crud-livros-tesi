from django.db import models

# Create your models here.
class Livro(models.Model):
    nome_livro = models.CharField(max_length=30)
    autor_livro = models.CharField(max_length=30)
    ano_publicacao = models.IntegerField()
    nota_livro = models.FloatField()
    obs_livro = models.CharField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
