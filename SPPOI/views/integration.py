from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from SPPOI.models import Projeto, Sistema, EstiloIntegracao


@require_http_methods(["GET"])
def render_integration(request, id):
    try:
        project = get_object_or_404(Projeto, pk=id)
        mSystems = Sistema.objects.filter(projeto=project).values()

        return render(request, 'registerIntegration.html', {
            'mSystems': mSystems,
            'project': project
        })

    except Exception as e:
        messages.error(request, f"Erro ao carregar a página de integração: {str(e)}")
        return HttpResponseRedirect(reverse('render_lab'))


@require_http_methods(["POST"])
def register(request, id):
    try:
        project = get_object_or_404(Projeto, pk=id)

        sistema_origem_id = request.POST.get("sistema_origem_id")
        sistema_destino_id = request.POST.get("sistema_destino_id")
        estilo = request.POST.get("estilo", "").strip()

        if not sistema_origem_id or not sistema_destino_id or not estilo:
            raise ValueError("Campos obrigatórios não preenchidos.")

        if sistema_origem_id == sistema_destino_id:
            raise ValueError("O sistema de origem e destino não podem ser iguais.")

        sistema_origem = get_object_or_404(Sistema, pk=sistema_origem_id)
        sistema_destino = get_object_or_404(Sistema, pk=sistema_destino_id)

        detalhes = {}

        if estilo == "Banco Compartilhado":
            detalhes = {
                "tipo_banco": request.POST.get("tipo_banco", "").strip(),
                "host": request.POST.get("host", "").strip(),
                "porta": request.POST.get("porta", "").strip(),
                "nome_banco": request.POST.get("nome_banco", "").strip(),
                "usuario": request.POST.get("usuario", "").strip(),
                "senha": request.POST.get("senha", "").strip(),
                "tabelas_compartilhadas": request.POST.get("tabelas_compartilhadas", "").strip(),
                "sincronizacao": request.POST.get("sincronizacao", "").strip(),
            }
        elif estilo == "Mensageria":
            detalhes = {
                "broker": request.POST.get("broker", "").strip(),
                "topicos_filas": request.POST.get("topicos_filas", "").strip(),
                "formato_dados": request.POST.get("formato_mensagem", "").strip(),
            }
        elif estilo == "RPC":
            detalhes = {
                "tipo_rpc": request.POST.get("tipo_rpc", "").strip(),
                "metodos": request.POST.get("definicoes_metodos", "").strip(),
                "endpoint_rpc": request.POST.get("endpoint_rpc", "").strip(),
            }
        elif estilo == "Troca de Arquivos":
            detalhes = {
                "tipo_arquivo": request.POST.get("tipo_arquivo", "").strip(),
                "protocolo": request.POST.get("protocolo", "").strip(),
                "local_armazenamento": request.POST.get("local_armazenamento", "").strip(),
                "transformacao": request.POST.get("transformacao_arquivo", "").strip(),
            }
        else:
            raise ValueError("Estilo de integração inválido ou não reconhecido.")

        EstiloIntegracao.objects.create(
            projeto=project,
            sistema_origem=sistema_origem,
            sistema_destino=sistema_destino,
            estilo=estilo,
            detalhes=detalhes
        )

        messages.success(request, "Integração registrada com sucesso.")
        return HttpResponseRedirect(reverse('render_lab'))

    except ValueError as ve:
        messages.error(request, str(ve))
    except Exception as e:
        messages.error(request, f"Ocorreu um erro inesperado: {str(e)}")

    # Em caso de erro, recarregar a página com os dados e a mensagem
    mSystems = Sistema.objects.filter(projeto=project).values()
    return render(request, 'registerIntegration.html', {
        'mSystems': mSystems,
        'project': project
    })
