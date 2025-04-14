from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, JsonResponse
from django.utils.timezone import now
from django.shortcuts import get_object_or_404, render
import json
from SPPOI.models import Projeto, Sistema, Interface, EstiloIntegracao

@csrf_exempt
def render_interface(request, id):
    project = get_object_or_404(Projeto, pk=id)
    mSystems = Sistema.objects.filter(projeto=project).values()

    context = {
        'mSystems': mSystems,
        'project': project
    }

    template = render(request,'registerInterface.html', context)
    return template

@csrf_exempt
def register(request, id):
    if request.method == "POST":
        project = get_object_or_404(Projeto, pk=id)
        system_id = request.POST.get('sistema_id')
        system = get_object_or_404(Sistema, pk=system_id)

        data = {
            "projeto": project,
            "sistema": system,
            "nome": request.POST.get("nome", ""),
            "tipo": request.POST.get("tipo", ""),
            "endpoint": request.POST.get("endpoint", ""),
            "formato_dados": request.POST.get("formato_dados", ""),
            "metodos_permitidos": request.POST.get("metodos_permitidos", ""),
            "esquema": request.POST.get("esquema", ""),
            "exemplo_dados": request.POST.get("exemplo_dados", ""),
            "operacoes_suportadas": request.POST.get("operacoes_suportadas", ""),
            "autenticacao": ", ".join(request.POST.getlist("autenticacao[]")),
            "throttling": request.POST.get("throttling", "")
        }

        Interface.objects.create(**data)
        return HttpResponseRedirect(reverse('render_lab'))

    return HttpResponseRedirect(reverse('render_lab'))