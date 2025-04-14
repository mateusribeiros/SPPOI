from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET
from django.contrib import messages
from SPPOI.models import Projeto

@require_GET
def index(request):
    try:
        return render(request, 'index.html')
    except Exception as e:
        messages.error(request, f"Erro ao carregar a página inicial: {str(e)}")
        return render(request, 'index.html')
    
@require_http_methods(["GET"])
def render_lab(request):
    try:
        project = Projeto.objects.all().values()

        return render(request, 'lab.html', {
            'project': project
        })

    except Exception as e:
        messages.error(request, f"Erro ao carregar os projetos: {str(e)}")
        return render(request, 'lab.html', {'project': []})