from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Livro
from .controller import LivroController


def listar_livros(request):
    livros = LivroController.listar()

    return render(request, "livros.html", {
        "livros": livros
    })

def cadastrar_livros():
    return render()

def editar_livros():
    return render()

def excluir_livros():
    return render()

