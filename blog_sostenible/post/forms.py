from django import forms
from .models import Post, Comentario

class FiltroTitulo(forms.Form):
    titulo = forms.CharField(max_length=200, required=False)

class FiltroCategoria(forms.Form):
    titulo = forms.CharField(max_length=200, required=False)

class FiltroComentario(forms.Form):
    texto = forms.CharField(max_length=200, required=False)

class FiltroFecha(forms.Form):
    desde= forms.DateField(required=False)
    hasta = forms.DateField(required=False)
    
class FilterForm(forms.Form):
    FILTER_CHOICES = (
        ('1', 'Fin de la pobreza'),
        ('2', 'Hambre cero'),
        ('3', 'Salud y bienestar'),
        ('4', 'Educación de calidad'),
        ('5', 'Igualdad de género'),
        ('6', 'Agua limpia y saneamiento'),
        ('7', 'Energía asequible y no contaminante'),
        ('8', 'Trabajo decente y crecimiento económico'),
        ('9', 'Industria, innovación e infraestructura'),
        ('10', 'reducir las desigualdades'),
        ('11', 'Ciudades y comonidades sostenibles'),
        ('12', 'Producción y consumo responsables'),
    )

    Categorias = forms.ChoiceField(choices = FILTER_CHOICES)
 
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
        
   
   
    

   