from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, JsonResponse
from django.utils.timezone import now
from django.shortcuts import get_object_or_404, render
import json
from SPPOI.models import Projeto, Sistema, Interface, EstiloIntegracao

@csrf_exempt
def render_system(request, id):
    project = get_object_or_404(Projeto, pk=id)

    context = {
        'project': project
    }

    template = render(request,'registerSystem.html', context)
    return template
    
@csrf_exempt
def register(request, id):
    if request.method == "POST":
        project = get_object_or_404(Projeto, pk=id)

        data = {
            "projeto": project,
            "nome": request.POST.get('name', ''),
            "descricao": request.POST.get('description', ''),
            "tipo": request.POST.get('type', ''),
            "versao": request.POST.get('version', ''),
            "funcionalidade_principal": request.POST.get('main_funcionality', ''),
            "protocolos_suportados": ", ".join(request.POST.getlist('protocolos[]')),
            "capacidades_dados": ", ".join(request.POST.getlist('data_manipulation_format[]')),
            "email_responsavel": request.POST.get('responsible_mail', ''),
            "contato_responsavel": request.POST.get('responsible_phone', ''),
            "mantenedor": request.POST.get('maintainer', ''),
            "requisitos_autenticacao": ", ".join(request.POST.getlist('authentication_requirements[]'))
        }

        Sistema.objects.create(**data)

        return HttpResponseRedirect(reverse('render_lab'))

    return HttpResponseRedirect(reverse('render_lab'))


@csrf_exempt
def update(request, id):
    return "implementar"

@csrf_exempt
def delete(request, id):
    return "implementar"
