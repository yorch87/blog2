from django.shortcuts import render
from categoria.models import Categoria

# Create your views here.
def listar_categorias(request):
        categorias = Categoria.objects.all()
        contexto = {"lista_categorias": categorias} 
        template = "categorias.html"
        
        return render(request, template, contexto)


