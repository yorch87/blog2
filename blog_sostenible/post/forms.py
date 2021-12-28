from django import forms
from .models import Post, Comentario
 
 
class PostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        #fields = "__all__"
        exclude = "autor",

class ComentarioModelForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = "__all__"
   
   
    

   