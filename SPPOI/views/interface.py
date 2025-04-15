from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect, JsonResponse, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from SPPOI.models import Projeto, Sistema, Interface

@require_http_methods(["GET"])
def render_interface(request, id):
    try:
        project = get_object_or_404(Projeto, pk=id)
        mSystems = Sistema.objects.filter(projeto=project).values()

        return render(request, 'registerInterface.html', {
            'mSystems': mSystems,
            'project': project
        })

    except Exception as e:
        messages.error(request, f"Erro ao carregar a interface: {str(e)}")
        return redirect(reverse('render_project', kwargs={'id': id}))


@require_http_methods(["POST"])
def register(request, id):
    try:
        project = get_object_or_404(Projeto, pk=id)

        # Validação de sistema
        system_id = request.POST.get('sistema_id')
        if not system_id:
            raise ValueError("Sistema não selecionado.")

        system = get_object_or_404(Sistema, pk=system_id)

        # Campos obrigatórios
        nome = request.POST.get("nome", "").strip()
        tipo = request.POST.get("tipo", "").strip()

        if not nome or not tipo:
            raise ValueError("Os campos 'nome' e 'tipo' são obrigatórios.")

        interface = Interface.objects.create(
            projeto=project,
            sistema=system,
            nome=nome,
            tipo=tipo,
            endpoint=request.POST.get("endpoint", "").strip(),
            formato_dados=request.POST.get("formato_dados", "").strip(),
            metodos_permitidos=request.POST.get("metodos_permitidos", "").strip(),
            esquema=request.POST.get("esquema", "").strip(),
            exemplo_dados=request.POST.get("exemplo_dados", "").strip(),
            operacoes_suportadas=request.POST.get("operacoes_suportadas", "").strip(),
            autenticacao=", ".join(request.POST.getlist("autenticacao[]")),
            throttling=request.POST.get("throttling", "").strip()
        )
    
        messages.success(request, "Interface registrada com sucesso.")
        return redirect(reverse('render_project', kwargs={'id': id}))

    except ValueError as ve:
        messages.error(request, f"Erro: {str(ve)}")
    except Exception as e:
        messages.error(request, f"Ocorreu um erro inesperado: {str(e)}")

    return HttpResponseRedirect(reverse('render_interface', args=[id]))


@require_http_methods(["POST"])
def delete(request, id, idInterface):
    try:
        project = get_object_or_404(Projeto, pk=id)
        interface = get_object_or_404(Interface, id=idInterface, projeto=project)
        interface.delete()

        messages.success(request, f"Interface deletada com sucesso.")
    
    except Interface.DoesNotExist:
        messages.error(request, "A interface não foi encontrada.")
    
    except Projeto.DoesNotExist:
        messages.error(request, "Projeto não encontrado.")
    
    except Exception as e:
        messages.error(request, f"Ocorreu um erro ao deletar a interface: {str(e)}")

    return redirect('render_project', id=id)

@require_http_methods(["POST"])
def update(request, id, idInterface):
    project = get_object_or_404(Projeto, pk=id)
    interface = get_object_or_404(Interface, id=idInterface, projeto=project)
    mSystems = Sistema.objects.filter(projeto=project).values()
    
    context = {
        'project': project,
        'interface': interface,
        'mSystems': mSystems
    }

    return render(request, 'updateInterface.html', context)

@require_http_methods(["POST"])
def updateData(request, id, idInterface):
    try:
        project = get_object_or_404(Projeto, pk=id)
        updateInterface = get_object_or_404(Interface, id=idInterface, projeto=project)

        updateInterface.projeto = project

        sistema_id = request.POST.get('sistema_id')
        if not sistema_id:
            raise ValueError("Sistema não selecionado.")

        sistema = get_object_or_404(Sistema, pk=sistema_id)
        updateInterface.sistema = sistema

        # Campos
        updateInterface.nome = request.POST.get("nome", "").strip()
        updateInterface.tipo = request.POST.get("tipo", "").strip()
        updateInterface.endpoint=request.POST.get("endpoint", "").strip()
        updateInterface.formato_dados=request.POST.get("formato_dados", "").strip()
        updateInterface.metodos_permitidos=request.POST.get("metodos_permitidos", "").strip()
        updateInterface.esquema=request.POST.get("esquema", "").strip()
        updateInterface.exemplo_dados=request.POST.get("exemplo_dados", "").strip()
        updateInterface.operacoes_suportadas=request.POST.get("operacoes_suportadas", "").strip()
        updateInterface.autenticacao=", ".join(request.POST.getlist("autenticacao[]"))
        updateInterface.throttling=request.POST.get("throttling", "").strip()

        if not updateInterface.nome or not updateInterface.tipo:
            raise ValueError("Os campos 'nome' e 'tipo' são obrigatórios.")

        updateInterface.save()
    
        messages.success(request, "Interface atualizada com sucesso.")
        return redirect(reverse('render_project', kwargs={'id': id}))

    except ValueError as ve:
        messages.error(request, str(ve))
    except Interface.DoesNotExist:
        messages.error(request, "A Interface não foi encontrada.")
    except Projeto.DoesNotExist:
        messages.error(request, "Projeto não encontrado.")
    except Exception as e:
        messages.error(request, f"Ocorreu um erro ao atualizar a Interface: {str(e)}")

    project = get_object_or_404(Projeto, pk=id)
    interface = get_object_or_404(Interface, id=idInterface, projeto=project)
    mSystems = Sistema.objects.filter(projeto=project).values()
    
    context = {
        'project': project,
        'interface': interface,
        'mSystems': mSystems
    }

    return render(request, 'updateInterface.html', context)