from django import forms
from .models import Livro
class FormCadastro(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['nome_livro', 'autor_livro', 'ano_publicacao', 'nota_livro', 'obs_livro', 'data_inicio', 'data_fim']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'data_fim': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nome_livro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do livro'}),
            'autor_livro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do autor'}),
            'ano_publicacao': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 2020'}),
            'nota_livro': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'max': '10'}),
            'obs_livro': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Observações (opcional)'}),
        }
        labels = {
            'nome_livro': 'Nome do Livro',
            'autor_livro': 'Autor(a)',
            'ano_publicacao': 'Ano de Publicação',
            'nota_livro': 'Nota (0-10)',
            'obs_livro': 'Observações',
            'data_inicio': 'Data de Início da Leitura',
            'data_fim': 'Data de Conclusão',
        }
        