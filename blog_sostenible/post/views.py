from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from post.models import Post, Comentario
from categoria.models import Categoria
from .forms import PostModelForm, ComentarioModelForm, FiltroTitulo, FiltroFecha
#from django.contrib.messages import  messages



# Create your views here.
def vista_redirige(request):
    return redirect("/posts/")

def postsxcategoria(request,id):

        categoria = Categoria.objects.get(id=id)
        posts = Post.objects.filter(categoria=categoria)
        template = "postsxcategoria.html"
        contexto = {"categoria":categoria,"posts":posts}
        return render(request, template, contexto)

def listar_posts(request):
        formulario = FiltroTitulo(request.GET or None)
        formulariofecha = FiltroFecha(request.GET or None)
        # filtro_titulo = formulario.cleaned_data["titulo"]
        # desde = formulariofecha.cleaned_data["desde"]
        # hasta = formulariofecha.cleaned_data["hasta"]
        desde = None
        hasta = None
        # if desde:
        #     posts.filter(creado__gte=desde)  #gte mayor o igual
        # if hasta:
        #     posts.filter(creado__lte=hasta) #lte menor o igual
        
        if formulario.is_valid() and formulario.data != None :
            print("formulario valido: ", formulario.cleaned_data)
            filtro_titulo = formulario.cleaned_data["titulo"]
            #posts= Post.objects.filter(titulo__icontains = filtro_titulo)
            posts= Post.objects.filter(titulo__icontains = filtro_titulo)
            posts = posts.order_by("-creado") 
        else:
            print(formulario.errors)    
            print(formulariofecha.errors)
            posts = Post.objects.all().order_by("-creado")  

        
        if formulariofecha.data != None and formulariofecha.is_valid(): 
            print("formulario valido: ", formulariofecha.cleaned_data)
            desde = formulariofecha.cleaned_data.get("desde", None)
            hasta = formulariofecha.cleaned_data.get("hasta", None)
            #posts= Post.objects.filter(creado__range=(desde, hasta))
            if desde:
                posts = posts.filter(creado__gte=desde)  #gte mayor o igual
            if hasta:
                posts = posts.filter(creado__lte=hasta)
            #posts= posts.filter(creado__range=(desde, hasta))
            posts = posts.order_by("-creado") 
        else:
            print(formulario.errors)    
            print(formulariofecha.errors)
            posts = Post.objects.all().order_by("-creado")  
        
            
            
            

        
              
               
        contexto = {"lista_posts": posts, "form": formulario, "formfecha": formulariofecha} 
        template = "posts.html"
        
        return render(request, template, contexto)

def ver_post(request,id):
        post = Post.objects.get(id=id)
        comentarios = post.comentario_set.all().order_by("-creado")
        contexto = {"post":post, "comentarios":comentarios}
        template = "ver_detalle_post.html"
        
        return render(request, template,contexto)

@login_required(login_url='/social/login')
def crear_post(request):
    if request.user.id == 2:
        return redirect("/posts/")    

    if request.method == "POST":
        
        form_obj = PostModelForm(request.POST)
                
        if form_obj.is_valid():
                     
            post=form_obj.save(commit=False)
            post.autor=request.user
            post.save()
            return redirect("/posts/")
    formulario_post = PostModelForm()
    contexto = {"formulario_post":formulario_post}
    return render(request, 'crear_post.html',  contexto )


@login_required(login_url='/social/login')
def editar_post(request,id):
        post_obj = Post.objects.filter(id=id).first()
        if not request.user == post_obj.autor and not request.user.id == 1:
                return redirect("/posts/")
        if request.method == "POST":
                 
                form_obj = PostModelForm(request.POST, instance=post_obj)
                if form_obj.is_valid():
                        form_obj.save()
                return redirect("/posts/")
        
        form_obj = PostModelForm(instance=post_obj)
        contexto = {"form_obj":form_obj}
                                                               
        return render(request, "editar_post.html", contexto)

@login_required(login_url='/social/login')
def eliminar_post(request,id):
        post = Post.objects.get(id=id)
        if not request.user == post.autor and not request.user.id == 1:
                return redirect("/posts/")
       
        post.delete()
        template = "ver_detalle_post.html"
        #messages.success(request, "Post eliminado correctamente")

        return redirect("/posts/")

@login_required(login_url='/social/login')
def crear_comentario(request,id):
    post_id = str(id)
       
    if request.method == "POST":
        
        form_obj = ComentarioModelForm(request.POST)
                
        if form_obj.is_valid():

            comen=form_obj.save(commit=False) 
            comen.autor=request.user
            comen.post_id = id       
            form_obj.save()
            return redirect("/posts/ver_detalle_post/"+post_id)
    formulario_comentario = ComentarioModelForm()
    contexto = {"formulario_comentario":formulario_comentario}
    return render(request, 'crear_comentario.html',  contexto )
        


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



def eliminar_comentario(request,id):
        
        comentario = Comentario.objects.get(id=id)
        post_id = str(comentario.post_id)
        comentario.delete()
        template = "ver_detalle_post.html"
        #messages.success(request, "Post eliminado correctamente")

        return redirect("/posts/")


     
        
   



