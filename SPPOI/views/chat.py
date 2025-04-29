from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from SPPOI.models import Projeto, Sistema, Interface, EstiloIntegracao
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os
import requests
from django.conf import settings

@require_http_methods(["GET", "POST"])
def render_chat(request, id):
    try:
        # Buscar os dados do projeto e relacionados
        project, mSystems, mInterfaces, mIntegrationStyles = get_project_data(id)

        # Inicializa valores padrão
        prompt = None
        ai_response = None

        # Se for POST, significa que o usuário clicou para consultar a IA
        if request.method == "POST":
            # Criar prompt
            prompt = create_prompt(project, mSystems, mInterfaces, mIntegrationStyles)
            # Obter resposta da IA
            ai_response = get_ai_response(prompt)

        context = {
            'project': project,
            'mSystems': mSystems,
            'mInterfaces': mInterfaces,
            'mIntegrationStyles': mIntegrationStyles,
            'prompt': prompt,
            'ai_response': ai_response,
        }

        return render(request, 'chat.html', context)

    except Exception as e:
        messages.error(request, f"Erro ao carregar o projeto: {str(e)}")
        return HttpResponseRedirect(reverse('render_project', kwargs={'id': id}))

    
def create_prompt(project, mSystems, mInterfaces, mIntegrationStyles):
    prompt = f"""Você é uma IA especialista de alto nível em integração de sistemas, arquitetura de software e interoperabilidade. Seu objetivo é analisar ambientes de sistemas com foco em **melhorias, boas práticas e pontos críticos de atenção**, com base nos dados fornecidos.

    ### Contexto do Projeto
    Projeto:
    - Nome: {project.nome}

    Sistemas:
    """
    for system in mSystems:
        prompt += (
            f"- {system['nome']} (Tipo: {system['tipo']}, Versão: {system['versao']}, "
            f"Função Principal: {system['funcionalidade_principal']}, Protocolos Suportados: {system['protocolos_suportados']}, "
            f"Capacidades de Dados: {system['capacidades_dados']}, Mantenedor: {system['mantenedor']}, "
            f"Autenticação: {system['requisitos_autenticacao']})\n"
        )

    prompt += "\nInterfaces:\n"
    for interface in mInterfaces:
        prompt += (
            f"- {interface['nome']} (Tipo: {interface['tipo']}, Endpoint: {interface['endpoint']}, "
            f"Formato de Dados: {interface['formato_dados']}, Métodos Permitidos: {interface['metodos_permitidos']}, "
            f"Autenticação: {interface['autenticacao']}, Operações Suportadas: {interface['operacoes_suportadas']})\n"
        )

    prompt += "\nEstilos de Integração:\n"
    for style in mIntegrationStyles:
        prompt += (
            f"- {style.estilo} (De: {style.sistema_origem.nome} → Para: {style.sistema_destino.nome}, "
            f"Detalhes: {style.detalhes})\n"
        )

    prompt += """

    ### Tarefas
    1. Analise criticamente o ambiente apresentado com base em boas práticas reconhecidas da indústria (ex: desacoplamento, padronização, segurança, escalabilidade).
    2. Sugira melhorias **específicas**, **concretas** e **executáveis** nos seguintes aspectos:
    - Sistemas: arquitetura, segurança, capacidade de manutenção, uso de protocolos e dados.
    - Interfaces: padronização, resiliência, versionamento, documentação, escalabilidade.
    - Estilos de Integração: eficiência, sincronismo, acoplamento, modernização, event-driven, API-first.
    3. Aponte riscos ou fragilidades que podem comprometer a interoperabilidade ou escalabilidade futura.
    4. Forneça dicas práticas ou padrões arquiteturais que poderiam ser adotados para melhorar a integração.

    ### Requisitos de Resposta
    - Escreva em **português brasileiro**, de forma clara, técnica e objetiva.
    - Não inclua saudações, desculpas ou referências a você mesmo.
    - Não faça suposições sobre o que o usuário já sabe ou não. Foque na clareza e na precisão técnica.
    - Apresente uma análise detalhada, porém gerencie de maneira econômica o espaço de resposta.
    - Gerencie a resposta para possuir no máximo 2000 tokens, sem encerrar a resposta abruptamente e contendo uma conclusão clara.
    - Evite repetições e redundâncias. Cada frase deve agregar valor à análise.
    - Finalize a resposta após a conclusão. **Não repita, não reinicie, nem ultrapasse os 2000 tokens.**
    - Lembre-se que o seu público são **desenvolvedores e arquitetos de software**.
    - Estruture a resposta assim:
    - **Nomes Extraídos**: [lista separada por vírgulas]
    - **Análise e Melhorias**: [tópicos com bullet points]
    """

    return prompt


def get_ai_response(prompt):
    # Pegue o token do ambiente
    hf_token = settings.HF_API_TOKEN  # ou use os.environ.get('HF_API_TOKEN') se preferir
    
    if not hf_token:
        raise Exception("Token da HuggingFace não encontrado nas variáveis de ambiente.")

    # Escolha o modelo que aceita prompts grandes (exemplo: mistralai/Mistral-7B-v0.1)
    model_id = "NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO"

    api_url = f"https://router.huggingface.co/together/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {hf_token}",
        "Content-Type": "application/json"
    }
    

    payload = {
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "model": model_id,
        "max_tokens": 2000,
    }


    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code != 200:
        print(f"Erro na requisição: {response.status_code}")
        print(f"Detalhes do erro: {response.text}")
        raise Exception(f"Erro na API da HuggingFace: {response.status_code} - {response.text}")


    result = response.json()

    generated_text = result["choices"][0]["message"]["content"]

    return generated_text

def get_project_data(project_id):
    # Busca o projeto e seus dados internos 
    project = get_object_or_404(Projeto, pk=project_id)
    mSystems = Sistema.objects.filter(projeto=project).values()
    mInterfaces = Interface.objects.filter(projeto=project).values()
    mIntegrationStyles = EstiloIntegracao.objects.filter(projeto=project)
    
    return project, mSystems, mInterfaces, mIntegrationStyles

