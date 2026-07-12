from .models import Livro

class LivroController:

    @staticmethod
    def listar():
        return Livro.objects.all()

    @staticmethod
    def cadastrar(dados):
        return Livro.objects.create(
            titulo=dados["titulo"],
            autor=dados["autor"],
            ano=dados["ano"]
        )