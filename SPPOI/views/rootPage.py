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
        if not request.session.session_key:
            request.session.save()

        session_key = request.session.session_key

        project = Projeto.objects.filter(session_key=session_key).values()

        return render(request, 'lab.html', {
            'project': project
        })

    except Exception as e:
        messages.error(request, f"Erro ao carregar os projetos: {str(e)}")
        return render(request, 'lab.html', {'project': []})
    