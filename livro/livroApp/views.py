from django.shortcuts import render, redirect, get_object_or_404
from .controller import LivroController
from .forms import FormCadastro
from .models import Livro

def listar_livros(request):
    livros = LivroController.listar()

    return render(request, "livros.html", {
        "livros": livros
    })

def cadastrar_livro(request):
    form = FormCadastro()

    if request.method == "POST":
        form = FormCadastro(request.POST)
        if form.is_valid():
            LivroController.cadastrar(form)
            return redirect("/")
    
    return render(request, "cadastro.html", {"form": form})

def editar_livros(request, id_livro):
    livro = get_object_or_404(Livro, pk=id_livro)

    if request.method == "POST":
        form = FormCadastro(request.POST, instance=livro)
        if form.is_valid():
            LivroController.editar(form)
            return redirect("/")
    else:
        form = FormCadastro(instance=livro)

    return render(request, "editar.html", {"form": form, "livro": livro})


def excluir_livros(request, id_livro):
    livro = get_object_or_404(Livro, pk=id_livro)

    if request.method == "POST":
        LivroController.excluir(id_livro)
        return redirect("/")

    return render(request, "excluir.html", {"livro": livro})

