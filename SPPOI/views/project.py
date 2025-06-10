from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from SPPOI.models import Projeto, Sistema, Interface, EstiloIntegracao

def create_session(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key


@require_http_methods(["GET"])
def render_project(request, id):
    try:
        project = get_object_or_404(Projeto, pk=id)
        mSystems = Sistema.objects.filter(projeto=project).values()
        mInterfaces = Interface.objects.filter(projeto=project).values()
        mIntegrationStyles = EstiloIntegracao.objects.filter(projeto=project)

        context = {
            'project': project,
            'mSystems': mSystems,
            'mInterfaces': mInterfaces,
            'mIntegrationStyles': mIntegrationStyles,
        }

        return render(request, 'project.html', context)

    except Exception as e:
        messages.error(request, f"Erro ao carregar o projeto: {str(e)}")
        return HttpResponseRedirect(reverse('render_lab'))


@require_http_methods(["POST"])
def register_project(request):
    try:
        session_key = create_session(request)
        project_name = request.POST.get("project_name", "")

        if not project_name:
            messages.error(request, "O nome do projeto é obrigatório.")
            return HttpResponseRedirect(reverse('render_lab'))

        Projeto.objects.create(
            nome=project_name,
            session_key=session_key
        )

        messages.success(request, "Projeto criado com sucesso!")
        return HttpResponseRedirect(reverse('render_lab'))

    except Exception as e:
        messages.error(request, f"Erro ao criar projeto: {str(e)}")
        return HttpResponseRedirect(reverse('render_lab'))
    
@require_http_methods(["POST"])
def delete(request, id):
    try:
        project = get_object_or_404(Projeto, pk=id)
        project.delete()
        messages.success(request, f"Projeto deletado com sucesso.")

    except Exception as e:
        messages.error(request, f"Ocorreu um erro ao deletar o projeto: {str(e)}")

    return redirect('render_lab')

@require_http_methods(["POST"])
def update(request, id):
    try:
        project = get_object_or_404(Projeto, pk=id)
        new_name = request.POST.get("project_name", "").strip()

        if not new_name:
            messages.error(request, "O nome do projeto é obrigatório.")
            return HttpResponseRedirect(reverse('render_lab'))

        project.nome = new_name
        project.save()

        messages.success(request, "Projeto atualizado com sucesso!")
        return HttpResponseRedirect(reverse('render_lab'))

    except Exception as e:
        messages.error(request, f"Erro ao atualizar projeto: {str(e)}")
        return HttpResponseRedirect(reverse('render_lab'))