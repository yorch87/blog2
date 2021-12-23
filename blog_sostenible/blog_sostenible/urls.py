"""blog_sostenible URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from categoria import views
from post.views import listar_posts, ver_post, postsxcategoria, editar_post, eliminar_post, crear_post, crear_comentario, eliminar_comentario, editar_comentario

urlpatterns = [
    path('admin/', admin.site.urls),
    path("categorias/", views.listar_categorias),
    path("posts/", listar_posts),
    path("posts/ver_detalle_post/<int:id>", ver_post),
    path("posts/ver_detalle_post/editar/<int:id>", editar_post),
    path("posts/ver_detalle_post/eliminar/<int:id>", eliminar_post),
    path("posts/ver_detalle_post/eliminar_comentario/<int:id>", eliminar_comentario),
    path("posts/ver_detalle_post/editar_comentario/<int:id>", editar_comentario),
    path("posts/ver_detalle_post/crear_comentario/<int:id>", crear_comentario),
    path("posts/categoria/<int:id>", postsxcategoria),
    path("posts/categoria/ver_detalle_post/<int:id>", ver_post),
    path("posts/post/", crear_post),
        
    path("posts/post/ver_detalle_post/<int:id>", ver_post),
    
]
