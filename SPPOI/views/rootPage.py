from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET
from django.contrib import messages
from SPPOI.models import Projeto

def create_session(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key

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
        session_key = create_session(request)

        projects = Projeto.objects.filter(session_key=session_key)

        return render(request, 'lab.html', {
            'projects': projects
        })

    except Exception as e:
        messages.error(request, f"Erro ao carregar os projetos: {str(e)}")
        return render(request, 'lab.html', {'projects': []})
    