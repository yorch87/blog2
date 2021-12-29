from django import forms
from .models import Post, Comentario

class FiltroTitulo(forms.Form):
    titulo = forms.CharField(required=False)
    

 
class PostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        #fields = "__all__"
        exclude = "autor",

class ComentarioModelForm(forms.ModelForm):

    class Meta:
        model = Comentario
        #fields = "__all__"
        exclude = "autor","post",
        
   
   
    

   