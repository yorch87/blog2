from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField
from categoria.models import Categoria
from django.contrib.auth.models import User
#from django.db.models.DataTime import DataTime

# Create your models here.
class Post(models.Model):
        titulo = models.CharField(max_length=200, null=False, blank=False)
        autor = models.CharField(max_length=50, null=False, blank=False)
        #autor = models.ForeignKey(User, on_delete=models.CASCADE)
        texto = models.TextField()
        #created = DateField(auto_now_add=True)
        #updated = DateField(auto_now_add=True)

        #created = DateTimeField.auto_now_add



        categoria = models.ManyToManyField(Categoria)
        

        def __str__(self):
            return self.titulo + self.autor