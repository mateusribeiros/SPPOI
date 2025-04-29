from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from SPPOI.models import Projeto, Sistema


@require_http_methods(["GET"])
def render_system(request, id):
    try:
        project = get_object_or_404(Projeto, pk=id)

        return render(request, 'registerSystem.html', {
            'project': project
        })

    except Exception as e:
        messages.error(request, f"Erro ao carregar a página de registro de sistema: {str(e)}")
        return redirect(reverse('render_project', kwargs={'id': id}))


@require_http_methods(["POST"])
def register(request, id):
    try:
        project = get_object_or_404(Projeto, pk=id)

        # Captura e validação básica de campos
        nome = request.POST.get('name', '').strip()
        if not nome:
            raise ValueError("O nome do sistema é obrigatório.")

        data = {
            "projeto": project,
            "nome": nome,
            "descricao": request.POST.get('description', '').strip(),
            "tipo": request.POST.get('type', '').strip(),
            "versao": request.POST.get('version', '').strip(),
            "funcionalidade_principal": request.POST.get('main_funcionality', '').strip(),
            "protocolos_suportados": ", ".join(request.POST.getlist('protocolos[]')),
            "capacidades_dados": ", ".join(request.POST.getlist('data_manipulation_format[]')),
            "email_responsavel": request.POST.get('responsible_mail', '').strip(),
            "contato_responsavel": request.POST.get('responsible_phone', '').strip(),
            "mantenedor": request.POST.get('maintainer', '').strip(),
            "requisitos_autenticacao": ", ".join(request.POST.getlist('authentication_requirements[]'))
        }

        Sistema.objects.create(**data)
        messages.success(request, "Sistema registrado com sucesso.")
        return redirect(reverse('render_project', kwargs={'id': id}))

    except ValueError as ve:
        messages.error(request, str(ve))
    except Exception as e:
        messages.error(request, f"Ocorreu um erro inesperado ao registrar o sistema: {str(e)}")

    # Recarregar a página com dados em caso de erro
    project = get_object_or_404(Projeto, pk=id)
    return render(request, 'registerSystem.html', {
        'project': project
    })

@require_http_methods(["POST"])
def delete(request, id, idSystem):
    try:
        project = get_object_or_404(Projeto, pk=id)
        system = get_object_or_404(Sistema, id=idSystem, projeto=project)

        system.delete()
        messages.success(request, f"Sistema deletado com sucesso.")
    
    except Sistema.DoesNotExist:
        messages.error(request, "O sistema não foi encontrado.")
    
    except Projeto.DoesNotExist:
        messages.error(request, "Projeto não encontrado.")
    
    except Exception as e:
        messages.error(request, f"Ocorreu um erro ao deletar o sistema: {str(e)}")

    return redirect('render_project', id=id)

@require_http_methods(["POST"])
def update(request, id, idSystem):
    project = get_object_or_404(Projeto, pk=id)
    system = get_object_or_404(Sistema, id=idSystem, projeto=project)
    
    context = {
        'project': project,
        'system': system
    }

    return render(request, 'updateSystem.html', context)

@require_http_methods(["POST"])
def updateData(request, id, idSystem):
    try:
        project = get_object_or_404(Projeto, pk=id)
        updateSystem = get_object_or_404(Sistema, id=idSystem, projeto=project)

        # Captura e validação do nome
        nome = request.POST.get('name', '').strip()
        if not nome:
            raise ValueError("O nome do sistema é obrigatório.")

        # Atribuição direta ao objeto updateSystem
        updateSystem.nome = nome
        updateSystem.descricao = request.POST.get('description', '').strip()
        updateSystem.tipo = request.POST.get('type', '').strip()
        updateSystem.versao = request.POST.get('version', '').strip()
        updateSystem.funcionalidade_principal = request.POST.get('main_funcionality', '').strip()
        updateSystem.protocolos_suportados = ", ".join(request.POST.getlist('protocolos[]'))
        updateSystem.capacidades_dados = ", ".join(request.POST.getlist('data_manipulation_format[]'))
        updateSystem.email_responsavel = request.POST.get('responsible_mail', '').strip()
        updateSystem.contato_responsavel = request.POST.get('responsible_phone', '').strip()
        updateSystem.mantenedor = request.POST.get('maintainer', '').strip()
        updateSystem.requisitos_autenticacao = ", ".join(request.POST.getlist('authentication_requirements[]'))
        updateSystem.projeto = project

        updateSystem.save()
    
        messages.success(request, "Sistema atualizado com sucesso.")
        return redirect(reverse('render_project', kwargs={'id': id}))

    except ValueError as ve:
        messages.error(request, str(ve))
    except Sistema.DoesNotExist:
        messages.error(request, "O sistema não foi encontrado.")
    except Projeto.DoesNotExist:
        messages.error(request, "Projeto não encontrado.")
    except Exception as e:
        messages.error(request, f"Ocorreu um erro ao atualizar o Sistema: {str(e)}")

    project = get_object_or_404(Projeto, pk=id)
    system = get_object_or_404(Sistema, id=idSystem, projeto=project)
    
    context = {
        'project': project,
        'system': system
    }

    return render(request, 'updateSystem.html', context)