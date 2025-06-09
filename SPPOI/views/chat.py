import os
import requests
from django.conf import settings
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from langchain_chroma import Chroma

from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods
from SPPOI.models import Projeto, Sistema, Interface, EstiloIntegracao
from langchain_community.document_loaders import DirectoryLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from transformers import pipeline

DATA_PATH = os.path.join(settings.BASE_DIR, 'dados')
CHROMA_PATH = os.path.join(settings.BASE_DIR, 'chroma_db')
HF_TOKEN = settings.HF_API_TOKEN

os.makedirs(DATA_PATH, exist_ok=True)
os.makedirs(CHROMA_PATH, exist_ok=True)

@require_http_methods(["GET", "POST"])
def render_chat(request, id):
    try:
        project, mSystems, mInterfaces, mIntegrationStyles = get_project_data(id)

        prompt = None
        ai_response = None

        if request.method == "POST":
            system_prompt, user_prompt, prompt = create_prompt(project, mSystems, mInterfaces, mIntegrationStyles)
            
            if not os.path.exists(CHROMA_PATH):
                prepare_chroma_db()

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
        "Your goal is to analyze system environments with a focus on **improvements, best practices, integration and critical points of attention**, "
        "based exclusively on the provided data. Always: "
        "- Justify recommendations with clear technical trade-offs "
        "- Important:  Respond exclusively in Brazilian Portuguese, with correct syntax and semantics, as if written by a fluent technical writer;"
        "Write the entire response in correct Brazilian Portuguese, using fluent and professional grammatical structure, preserving only technical terms in English."
        "Never translate established technical domain terms into Portuguese;"
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

        Tasks
        1. Critical Analysis:
           - Evaluate using industry best practices (decoupling, standards, security, scalability, and other relevant patterns).
           - Analyze integration and interoperability aspects.
           - Identify underutilized capabilities in existing systems
        2. Improvement Suggestions (Specific, Concrete and Actionable):
            Cover:
            - Systems: architecture, security, maintainability, use of protocols and data.
            - Interfaces: standards, resilience, versioning, documentation, scalability.
            - Integration Styles: efficiency, synchronism, coupling, modernization, event-driven, API-first.
            For each recommendation:
            - All suggestions must be "clearly connected to an observed point in the scenario" and not generic.
            - Provide abstract implementation examples
            - Specify measurable KPIs for validation
            - Explain expected outcomes
        3. Point out any risks or weaknesses that could compromise future interoperability or scalability.
           - Identify interoperability/scalability threats with concrete impact scenarios
           - Flag data modeling inconsistencies showing actual data examples
           - Highlight technical debt
           - Explicitly mention if any modeling inconsistencies, duplications or outdated patterns are identified.
        4. Enhancement Patterns:
           - Recommend architectural patterns with implementation principles
           - Suggest observable metrics for each improvement
           - Provide phased migration approaches for legacy components

        Response Requirements
        - Depth: Technical justifications with trade-off analysis
        - Conclude the response properly. "Do not repeat, restart, or exceed the token limit."
        - Audience: Software architects/developers
        - Implementation examples must show abstract configuration patterns
        - Migration: Detail operational steps with environment impact analysis
        - Do not include greetings, apologies, or references to yourself.
        - Conciseness: < 1500 tokens, no repetition and ending with a clear conclusion and without cutting off abruptly.
        - Ensure a detailed yet concise response, using space efficiently.
        - Avoid repetition and redundancy—each sentence must add value.
        - Justify your suggestions based on recognized best practices and explain the reasoning behind each recommendation.
        - Connect each recommendation directly to the described scenario.
    """

    full_prompt = system_prompt + user_prompt

    return system_prompt, user_prompt, full_prompt


def get_ai_response(system_prompt, user_prompt):

    if not HF_TOKEN:
        raise Exception("Token da HuggingFace não encontrado nas variáveis de ambiente.")
    
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)

    results = db.similarity_search_with_relevance_scores(user_prompt, k=3)

    context_text = ""
    relevant_docs = [doc for doc, score in results if score >= 0.75]
    context_text = (
        "\n\n--\n\n".join([doc.page_content for doc in relevant_docs])
        if relevant_docs else "Nenhum contexto relevante encontrado."
    )

    prompt = f"""
    [CONTEXT START]
    {context_text}
    [CONTEXT END]

    User Question:
    {user_prompt}
    Write the entire response in correct Brazilian Portuguese, using fluent and professional grammatical structure, preserving only technical terms in English.
    """

    model_id = "microsoft/phi-4"
    api_url = f"https://router.huggingface.co/nebius/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        "model": model_id,
        "max_tokens": 2000,
        "temperature": 0.7,
        "top_p": 0.9,
    }

    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code != 200:
        print(f"Erro na requisição: {response.status_code}")
        print(f"Detalhes do erro: {response.text}")
        raise Exception(f"Erro na API da HuggingFace: {response.status_code} - {response.text}")

    result = response.json()

    generated_text = result["choices"][0]["message"]["content"]

    return generated_text

def prepare_chroma_db():
    loader = DirectoryLoader(DATA_PATH, glob="*.md")
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=500,
        length_function=len,
        add_start_index=True,
    )

    chunks = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = Chroma.from_documents(chunks, embedding=embeddings, persist_directory=CHROMA_PATH)
    db.persist()	

def get_project_data(project_id):
    project = get_object_or_404(Projeto, pk=project_id)
    mSystems = Sistema.objects.filter(projeto=project).values()
    mInterfaces = Interface.objects.filter(projeto=project).values()
    mIntegrationStyles = EstiloIntegracao.objects.filter(projeto=project)
    
    return project, mSystems, mInterfaces, mIntegrationStyles

