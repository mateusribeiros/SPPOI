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
            system_prompt, user_prompt, prompt = create_prompt(project, mSystems, mInterfaces, mIntegrationStyles)
            # Obter resposta da IA
            ai_response = get_ai_response(system_prompt, user_prompt)

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
    system_prompt = (
        "You are a highly specialized AI in systems integration, software architecture, and interoperability. "
        "Your goal is to analyze system environments with a focus on **improvements, best practices, and critical points of attention**, "
        "based on the provided data."
    )

    user_prompt = f"""### Project Context
    Project:
    - Name: {project.nome}

    Systems:
    """
    for system in mSystems:
        user_prompt += (
            f"- {system['nome']} (Type: {system['tipo']}, Version: {system['versao']}, "
            f"Main Functionality: {system['funcionalidade_principal']}, Supported Protocols: {system['protocolos_suportados']}, "
            f"Data Capabilities: {system['capacidades_dados']}, Maintainer: {system['mantenedor']}, "
            f"Authentication: {system['requisitos_autenticacao']})\n"
        )

    user_prompt += "\nInterfaces:\n"
    for interface in mInterfaces:
        user_prompt += (
            f"- {interface['nome']} (Type: {interface['tipo']}, Endpoint: {interface['endpoint']}, "
            f"Data Format: {interface['formato_dados']}, Allowed Methods: {interface['metodos_permitidos']}, "
            f"Authentication: {interface['autenticacao']}, Supported Operations: {interface['operacoes_suportadas']})\n"
        )

    user_prompt += "\nIntegration Styles:\n"
    for style in mIntegrationStyles:
        user_prompt += (
            f"- {style.estilo} (From: {style.sistema_origem.nome} → To: {style.sistema_destino.nome}, "
            f"Details: {style.detalhes})\n"
        )

    user_prompt += """

        ### Tasks
        1. Critically analyze the described environment using recognized industry best practices (e.g., decoupling, standardization, security, scalability).
           - The analysis must take into account **real data, duplication, protocol inconsistencies, authentication diversity**, and **data handling practices**.
        2. Provide **specific**, **concrete**, and **actionable** improvement suggestions for:
           - Systems: architecture, security, maintainability, use of protocols and data.
           - Interfaces: standardization, resilience, versioning, documentation, scalability.
           - Integration Styles: efficiency, synchronism, coupling, modernization, event-driven, API-first.
           - All suggestions must be **clearly connected to an observed point in the scenario** and not generic.
        3. Point out any risks or weaknesses that could compromise future interoperability or scalability.
           - Explicitly mention if any modeling inconsistencies, duplications or outdated patterns are identified.
        4. Offer practical tips or architectural patterns that could be adopted to enhance integration.
           - Suggest tools, frameworks or practices (e.g., ELK Stack, Prometheus, Kafka, Swagger) when appropriate.

        ### Response Requirements
        - Write the full response in **Brazilian Portuguese**, clearly, technically, and objectively.
        - Do not include greetings, apologies, or references to yourself.
        - Do not assume prior user knowledge; focus on technical clarity and precision.
        - Ensure a detailed yet concise response, using space efficiently.
        - Keep the output under **2000 tokens**, ending with a clear conclusion and without cutting off abruptly.
        - Avoid repetition and redundancy—each sentence must add value.
        - Conclude the response properly. **Do not repeat, restart, or exceed the token limit.**
        - Remember: the target audience is **software developers and architects**.
        - Justify your suggestions based on recognized best practices and explain the reasoning behind each recommendation.
        - Connect each recommendation directly to the described scenario.
        - Structure your response like this:
        - **Analysis and Recommendations**: [bullet points]
    """

    system_prompt = (
        f"<|im_start|>system<|im_sep|>\n{system_prompt}<|im_end|>\n"
    )
    user_prompt = (
        f"<|im_start|>user<|im_sep|>\n{user_prompt}<|im_end|>\n"
    )

    full_prompt = system_prompt + user_prompt

    return system_prompt, user_prompt, full_prompt



# def get_ai_response(prompt):

#     messages = [
#     {"role": "user", "content": prompt},
#     ]

#     pipe = pipeline("text-generation", model="microsoft/Phi-3-mini-128k-instruct", trust_remote_code=True)
#     ai_response = pipe(messages)

#     return ai_response

def get_ai_response(system_prompt, user_prompt):
    # Pegue o token do ambiente
    hf_token = settings.HF_API_TOKEN  # ou use os.environ.get('HF_API_TOKEN') se preferir
    
    if not hf_token:
        raise Exception("Token da HuggingFace não encontrado nas variáveis de ambiente.")

    # Escolha o modelo que aceita prompts grandes (exemplo: mistralai/Mistral-7B-v0.1)
    model_id = "microsoft/phi-4"

    api_url = f"https://router.huggingface.co/nebius/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {hf_token}",
        "Content-Type": "application/json"
    }
    

    payload = {
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
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

