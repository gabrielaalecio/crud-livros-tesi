from .models import Livro

class LivroController:

    @staticmethod
    def listar():
        return Livro.objects.all()

    @staticmethod
    def cadastrar(form):
        livro = form.save(commit=False)
        livro.save()

    @staticmethod
    def editar(form):
        livro = form.save(commit=False)
        livro.save()
        return livro

    @staticmethod
    def excluir(id_livro):
        livro = Livro.objects.get(pk=id_livro)
        livro.delete()