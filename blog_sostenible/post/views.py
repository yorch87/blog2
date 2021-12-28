from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from post.models import Post, Comentario
from categoria.models import Categoria
from .forms import PostModelForm, ComentarioModelForm
#from django.contrib.messages import  messages



# Create your views here.
def postsxcategoria(request,id):

        categoria = Categoria.objects.get(id=id)
        posts = Post.objects.filter(categoria=categoria)
        template = "postsxcategoria.html"
        contexto = {"categoria":categoria,"posts":posts}
        return render(request, template, contexto)

def listar_posts(request):
        posts = Post.objects.all().order_by("-creado")
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
                 
                form_obj = PostModelForm(request.POST, instance=post_obj)
                if form_obj.is_valid():
                        form_obj.save()
                return redirect("/posts/")
        
        form_obj = PostModelForm(instance=post_obj)
        contexto = {"form_obj":form_obj}
                                                               
        return render(request, "editar_post.html", contexto)

def editar_comentario(request,id):
        comentario_obj = Comentario.objects.filter(id=id).first()
        post_id = str(comentario_obj.post_id)

        if request.method == "POST":
                 
                form_obj = ComentarioModelForm(request.POST, instance=comentario_obj)
                if form_obj.is_valid():
                        form_obj.save()
                return redirect("/posts/ver_detalle_post/"+post_id)
        
        form_obj = ComentarioModelForm(instance=comentario_obj)
        contexto = {"form_obj":form_obj}
                                                               
        return render(request, "editar_comentario.html", contexto)


def eliminar_post(request,id):
        
        post = Post.objects.get(id=id)
        post.delete()
        template = "ver_detalle_post.html"
        #messages.success(request, "Post eliminado correctamente")

        return redirect("/posts/")

def eliminar_comentario(request,id):
        
        comentario = Comentario.objects.get(id=id)
        post_id = str(comentario.post_id)
        comentario.delete()
        template = "ver_detalle_post.html"
        #messages.success(request, "Post eliminado correctamente")

        return redirect("/posts/")

def crear_comentario(request,id):
    post_id = str(id)    
    if request.method == "POST":
        
        form_obj = ComentarioModelForm(request.POST)
                
        if form_obj.is_valid():
                     
            form_obj.save()
            return redirect("/posts/ver_detalle_post/"+post_id)
    formulario_comentario = ComentarioModelForm()
    contexto = {"formulario_comentario":formulario_comentario}
    return render(request, 'crear_comentario.html',  contexto )
        
     
        
   
@login_required(login_url='/social/login')
def crear_post(request):
    if request.method == "POST":
        
        form_obj = PostModelForm(request.POST)
                
        if form_obj.is_valid():
                     
            form_obj.save()
            return redirect("/posts/")
    formulario_post = PostModelForm()
    contexto = {"formulario_post":formulario_post}
    return render(request, 'crear_post.html',  contexto )


