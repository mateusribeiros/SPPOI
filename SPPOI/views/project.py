from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, JsonResponse
from django.utils.timezone import now
from django.shortcuts import get_object_or_404, render
import json
from SPPOI.models import Projeto, Sistema, Interface, EstiloIntegracao

# Verifica ou cria uma chave de sessão para o usuário
def createSession(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key

@csrf_exempt
def render_project(request, id):
    project = get_object_or_404(Projeto, pk=id)
    mSystems = Sistema.objects.filter(projeto=project).values()
    mInterfaces = Interface.objects.filter(projeto=project).values()
    mIntegrationStyles = EstiloIntegracao.objects.filter(projeto=project)

    context = {
        'mSystems': mSystems,
        'mInterfaces': mInterfaces,
        'mIntegrationStyles': mIntegrationStyles,
        'project': project,
    }

    return render(request, 'project.html', context)

@csrf_exempt   
def register_project(request):
    if request.method == "POST":
        session_key = createSession(request)

        data = {
            "nome": request.POST.get("project_name", ""),
            "session_key": session_key,
        }

        Projeto.objects.create(**data)

        return HttpResponseRedirect(reverse('render_lab'))

    return HttpResponseRedirect(reverse('render_lab'))

