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

@require_http_methods(["GET"])
def render_chat(request, id):
    try:
        # Buscar os dados do projeto
        project, mSystems, mInterfaces, mIntegrationStyles = get_project_data(id)

        # Criar o prompt para a IA
        prompt = create_prompt(project, mSystems, mInterfaces, mIntegrationStyles)

        # Obter a resposta da IA
        ai_response = get_ai_response(prompt)

        # Contexto para o template
        context = {
            'project': project,
            'mSystems': mSystems,
            'mInterfaces': mInterfaces,
            'mIntegrationStyles': mIntegrationStyles,
            'ai_response': ai_response,
        }

        return render(request, 'chat.html', context)

    except Exception as e:
        messages.error(request, f"Erro ao carregar o projeto: {str(e)}")
        return HttpResponseRedirect(reverse('render_project', kwargs={'id': id}))
    

# Implementação da IA generativa
def create_prompt(project, mSystems, mInterfaces, mIntegrationStyles):
    prompt = f"""You are a top-tier AI expert specialized in project analysis and improvement. Follow the instructions precisely.

### Context
Project:
- Name: {project.nome}
Systems:
"""
    for system in mSystems:
        prompt += (
            f"- {system['nome']} (Type: {system['tipo']}, Version: {system['versao']}, "
            f"Main Function: {system['funcionalidade_principal']}, Protocols: {system['protocolos_suportados']}, "
            f"Data Capabilities: {system['capacidades_dados']}, Maintainer: {system['mantenedor']}, "
            f"Auth Requirements: {system['requisitos_autenticacao']})\n"
        )

    prompt += "\nInterfaces:\n"
    for interface in mInterfaces:
        prompt += (
            f"- {interface['nome']} (Type: {interface['tipo']}, Endpoint: {interface['endpoint']}, "
            f"Data Format: {interface['formato_dados']}, Methods: {interface['metodos_permitidos']}, "
            f"Authentication: {interface['autenticacao']}, Operations: {interface['operacoes_suportadas']})\n"
        )

    prompt += "\nIntegration Styles:\n"
    for style in mIntegrationStyles:
        prompt += (
            f"- {style.estilo} (From: {style.sistema_origem.nome} → To: {style.sistema_destino.nome}, "
            f"Details: {style.detalhes})\n"
        )

    prompt += """

    ### Tasks
    1. Extract system, interface, and integration names into a **comma-separated list**. No extra text.
    2. Analyze the project based on industry best practices.
    3. Suggest **specific**, **concise**, and **actionable** improvements for:
    - Systems (architecture, security, maintainability)
    - Interfaces (design, robustness, scalability)
    - Integration styles (efficiency, decoupling, modernization)
    4. Write in clear English. No greetings, no disclaimers, no self-references.

    Respond in the following structure:
    - Extracted Names: [list]
    - Improvements: [bullet points]

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
        "max_tokens": 512,
    }


    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code != 200:
        print(f"Erro na requisição: {response.status_code}")
        print(f"Detalhes do erro: {response.text}")
        raise Exception(f"Erro na API da HuggingFace: {response.status_code} - {response.text}")


    result = response.json()

    generated_text = result["choices"][0]["message"]["content"]

    full_response = f"""=== Prompt ===
    {prompt}
    
    \n \n
    === AI Response ===
    {generated_text}
    """
    return full_response

def get_project_data(project_id):
    # Busca o projeto e seus dados internos 
    project = get_object_or_404(Projeto, pk=project_id)
    mSystems = Sistema.objects.filter(projeto=project).values()
    mInterfaces = Interface.objects.filter(projeto=project).values()
    mIntegrationStyles = EstiloIntegracao.objects.filter(projeto=project)
    
    return project, mSystems, mInterfaces, mIntegrationStyles

