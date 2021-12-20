from django.shortcuts import render
from post.models import Post

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
