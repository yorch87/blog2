from django.shortcuts import render
from django.shortcuts import redirect
from post.models import Post, Comentario
from categoria.models import Categoria
from .forms import PostModelForm
#from django.contrib.messages import  messages



# Create your views here.
def listar_posts(request):
        posts = Post.objects.all()
        contexto = {"lista_posts": posts} 
        template = "posts.html"
        
        return render(request, template, contexto)

def ver_post(request,id):
        post = Post.objects.get(id=id)
        comentarios = post.comentario_set.all().order_by("-creado")
        contexto = {"post":post, "comentarios":comentarios}
        template = "ver_detalle_post.html"
        
        return render(request, template,contexto)

def editar_post(request,id):
        post_obj = Post.objects.filter(id=id).first()

        if request.method == "POST":
                 # Al modificar los datos, puede pasar directamente la solicitud del paquete de datos del usuario.
                 #Pasar un ejemplo del objeto a modificar, ModelForm puede completar automáticamente la modificación de los datos.
                form_obj = PostModelForm(request.POST, instance=post_obj)
                if form_obj.is_valid():
                        form_obj.save()
                return redirect("/posts/")
        
        form_obj = PostModelForm(instance=post_obj)
        contexto = {"form_obj":form_obj}
                                                               
        return render(request, "editar_post.html", contexto)



def crear_post(request):
    if request.method == "POST":
        
        form_obj = PostModelForm(request.POST)
                
        if form_obj.is_valid():
                     
            form_obj.save()
            return redirect("/posts/")
    formulario_post = PostModelForm()
    contexto = {"formulario_post":formulario_post}
    return render(request, 'crear_post.html',  contexto )
  
  


def eliminar_post(request,id):
        
        post = Post.objects.get(id=id)
        post.delete()
        template = "ver_detalle_post.html"
        #messages.success(request, "Post eliminado correctamente")

        return redirect("/posts/")

def postsxcategoria(request,id):

        categoria = Categoria.objects.get(id=id)
        posts = Post.objects.filter(categoria=categoria)
        template = "postsxcategoria.html"
        contexto = {"categoria":categoria,"posts":posts}
        return render(request, template, contexto)


