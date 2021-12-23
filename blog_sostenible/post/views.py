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
        post_obj = Post.objects.filter(id=id).first()

        if request.method == "POST":
                 # Al modificar los datos, puede pasar directamente la solicitud del paquete de datos del usuario.
                 #Pasar un ejemplo del objeto a modificar, ModelForm puede completar automáticamente la modificación de los datos.
                form_obj = PostModelForm(request.POST, instance=post_obj)
                if form_obj.is_valid():
                        form_obj.save()
                return redirect("/posts/")
         # form_obj establece el valor inicializado a través de initial, por ejemplo, la función de edición de libros en el sistema de gestión de la biblioteca,
         # Haga clic en Editar y salte a la página de edición del libro. Después de saltar, debe completar la información correspondiente de la página con la información del libro a editar.
         # A diferencia del componente Form, ModelForm puede pasar directamente el objeto instanciado, sin la necesidad de convertir el objeto en un diccionario.
        form_obj = PostModelForm(instance=post_obj)
        contexto = {"form_obj":form_obj}
                                                               #locals () es una abreviatura de pares clave-valor de datos locales
        return render(request, "editar_post.html", contexto)

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
        post.delete()
        template = "ver_detalle_post.html"

        return redirect("/posts/")

def postsxcategoria(request,id):

        categoria = Categoria.objects.get(id=id)
        posts = Post.objects.filter(categoria=categoria)
        template = "postsxcategoria.html"
        contexto = {"categoria":categoria,"posts":posts}
        return render(request, template, contexto)


