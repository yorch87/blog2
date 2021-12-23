from django.shortcuts import render
from django.shortcuts import redirect
from post.models import Post
from categoria.models import Categoria
from .forms import PostModelForm



# Create your views here.
def listar_posts(request):
        posts = Post.objects.all()
        contexto = {"lista_posts": posts} 
        template = "posts.html"
        
        return render(request, template, contexto)

def ver_post(request,id):
        post = Post.objects.get(id=id)
        contexto = {"post":post}
        template = "ver_detalle_post.html"

        return render(request, template,contexto)

def editar_post(request,id):
        post = Post.objects.get(id=id)
        contexto = {"post":post}
        template = "ver_detalle_post.html"

        return render(request, template, contexto)

#def crear_post(request):
       # formulario_post = PostModelForm()
       # contexto = {"formulario_post":formulario_post}
       # template = "crear_post.html"

        #return render(request, template, contexto)

def crear_post(request):
    if request.method == "POST":
        # modelform puede obtener directamente el grupo de datos de la solicitud de interfaz.
                 #Cuando los parámetros se pasan al Modelform instanciado
        form_obj = PostModelForm(request.POST)
                 # Llame al método is_valid () para verificar los datos
        if form_obj.is_valid():
                         # Guardar directamente en la base de datos
            form_obj.save()
            return redirect("/posts/")
    formulario_post = PostModelForm()
    contexto = {"formulario_post":formulario_post}
    return render(request, 'crear_post.html',  contexto )
  
  


def eliminar_post(request,id):
        post = Post.objects.get(id=id)
        contexto = {"post":post}
        template = "ver_detalle_post.html"

        return render(request, template,contexto)

def postsxcategoria(request,id):

        categoria = Categoria.objects.get(id=id)
        posts = Post.objects.filter(categoria=categoria)
        template = "postsxcategoria.html"
        contexto = {"categoria":categoria,"posts":posts}
        return render(request, template, contexto)


