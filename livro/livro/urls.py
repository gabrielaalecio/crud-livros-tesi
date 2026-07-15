"""
URL configuration for livro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from livroApp import views

urlpatterns = [
    path('', views.listar_livros, name='listar'),
    path('adicionar/', views.cadastrar_livro, name='adicionar'),
    path('editar/<int:id_livro>/', views.editar_livros, name='editar'),
    path('excluir/<int:id_livro>/', views.excluir_livros, name='excluir'),
]
