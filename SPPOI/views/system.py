from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from SPPOI.models import Projeto, Sistema


def get_project_for_session_or_404(request, id):
    # Garante que a session_key exista
    if not request.session.session_key:
        request.session.save()
    session_key = request.session.session_key

    return get_object_or_404(Projeto, pk=id, session_key=session_key)


@require_http_methods(["GET"])
def render_system(request, id):
    try:
        project = get_project_for_session_or_404(request, id)

        return render(request, 'registerSystem.html', {
            'project': project
        })

    except Exception as e:
        messages.error(request, f"Erro ao carregar a página de registro de sistema: {str(e)}")
        return redirect(reverse('render_project', kwargs={'id': id}))


@require_http_methods(["POST"])
def register(request, id):
    try:
        project = get_project_for_session_or_404(request, id)

        nome = request.POST.get('name', '').strip()
        tipo = request.POST.get('type', '').strip()
        versao = request.POST.get('version', '').strip()
        protocolos = request.POST.getlist('protocolos[]')
        formatos = request.POST.getlist('data_manipulation_format[]')
        autenticacoes = request.POST.getlist('authentication_requirements[]')

        # Validações obrigatórias
        if not nome:
            raise ValueError("O nome do sistema é obrigatório.")
        if not tipo:
            raise ValueError("O tipo do sistema é obrigatório.")
        if not versao:
            raise ValueError("A versão do sistema é obrigatória.")
        if not protocolos:
            raise ValueError("É necessário informar pelo menos um protocolo suportado.")
        if not formatos:
            raise ValueError("É necessário informar pelo menos um formato de manipulação de dados.")
        if not autenticacoes:
            raise ValueError("É necessário informar pelo menos um requisito de autenticação.")

        data = {
            "projeto": project,
            "nome": nome,
            "descricao": request.POST.get('description', '').strip(),
            "tipo": tipo,
            "versao": versao,
            "funcionalidade_principal": request.POST.get('main_funcionality', '').strip(),
            "protocolos_suportados": ", ".join(protocolos),
            "capacidades_dados": ", ".join(formatos),
            "email_responsavel": request.POST.get('responsible_mail', '').strip(),
            "contato_responsavel": request.POST.get('responsible_phone', '').strip(),
            "mantenedor": request.POST.get('maintainer', '').strip(),
            "requisitos_autenticacao": ", ".join(autenticacoes)
        }

        Sistema.objects.create(**data)
        messages.success(request, "Sistema registrado com sucesso.")
        return redirect(reverse('render_project', kwargs={'id': id}))

    except ValueError as ve:
        messages.error(request, str(ve))
    except Exception as e:
        messages.error(request, f"Ocorreu um erro inesperado ao registrar o sistema: {str(e)}")

    project = get_project_for_session_or_404(request, id)
    return render(request, 'registerSystem.html', {
        'project': project
    })


@require_http_methods(["POST"])
def delete(request, id, idSystem):
    try:
        project = get_project_for_session_or_404(request, id)
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
    try:
        project = get_project_for_session_or_404(request, id)
        system = get_object_or_404(Sistema, id=idSystem, projeto=project)

        context = {
            'project': project,
            'system': system
        }

        return render(request, 'updateSystem.html', context)

    except Exception as e:
        messages.error(request, f"Erro ao carregar a página de atualização: {str(e)}")
        return redirect(reverse('render_project', kwargs={'id': id}))


@require_http_methods(["POST"])
def updateData(request, id, idSystem):
    try:
        project = get_project_for_session_or_404(request, id)
        updateSystem = get_object_or_404(Sistema, id=idSystem, projeto=project)

        nome = request.POST.get('name', '').strip()
        tipo = request.POST.get('type', '').strip()
        versao = request.POST.get('version', '').strip()
        protocolos = request.POST.getlist('protocolos[]')
        formatos = request.POST.getlist('data_manipulation_format[]')
        autenticacoes = request.POST.getlist('authentication_requirements[]')

        if not nome:
            raise ValueError("O nome do sistema é obrigatório.")
        if not tipo:
            raise ValueError("O tipo do sistema é obrigatório.")
        if not versao:
            raise ValueError("A versão do sistema é obrigatória.")
        if not protocolos:
            raise ValueError("É necessário informar pelo menos um protocolo suportado.")
        if not formatos:
            raise ValueError("É necessário informar pelo menos um formato de manipulação de dados.")
        if not autenticacoes:
            raise ValueError("É necessário informar pelo menos um requisito de autenticação.")

        updateSystem.nome = nome
        updateSystem.descricao = request.POST.get('description', '').strip()
        updateSystem.tipo = tipo
        updateSystem.versao = versao
        updateSystem.funcionalidade_principal = request.POST.get('main_funcionality', '').strip()
        updateSystem.protocolos_suportados = ", ".join(protocolos)
        updateSystem.capacidades_dados = ", ".join(formatos)
        updateSystem.email_responsavel = request.POST.get('responsible_mail', '').strip()
        updateSystem.contato_responsavel = request.POST.get('responsible_phone', '').strip()
        updateSystem.mantenedor = request.POST.get('maintainer', '').strip()
        updateSystem.requisitos_autenticacao = ", ".join(autenticacoes)

        updateSystem.save()
        messages.success(request, "Sistema atualizado com sucesso.")
        return redirect(reverse('render_project', kwargs={'id': id}))

    except ValueError as ve:
        messages.error(request, str(ve))
    except Exception as e:
        messages.error(request, f"Ocorreu um erro ao atualizar o sistema: {str(e)}")

    project = get_project_for_session_or_404(request, id)
    system = get_object_or_404(Sistema, id=idSystem, projeto=project)

    return render(request, 'updateSystem.html', {
        'project': project,
        'system': system
    })

