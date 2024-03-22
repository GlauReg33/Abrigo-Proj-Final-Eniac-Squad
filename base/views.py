from django.shortcuts import render
from django.http import HttpResponse
from base.forms import CadastroAdotantes
from base.models import CadastroAdotantes

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def cadastroAdotantes(request):
    success = False
    form = CadastroAdotantes(request.POST or None)
    if form.is_valid():
        success = True
        form.save()
    contexto = {
                'form': form,
                'success': success,
            }      
    return render(request, 'cadastroAdotantes.html',contexto)