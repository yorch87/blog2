from django.contrib import admin
from post.models import Post, Comentario


class PostAdmin(admin.ModelAdmin):
    list_display=("titulo", "autor", "texto", "creado", "modificado")

class ComentarioAdmin(admin.ModelAdmin):
    list_display=("texto", "autor", "creado", "modificado")


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comentario, ComentarioAdmin)
