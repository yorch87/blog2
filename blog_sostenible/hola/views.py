from django.shortcuts import render

def bienvenido(request):
        template = "index.html"
        contexto = {
            "nombre":"axel",
        }
        return render(request, template, contexto)
