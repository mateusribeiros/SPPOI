from django.db import models

class Sistema(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    tipo = models.CharField(max_length=50)
    versao = models.CharField(max_length=20)
    funcionalidade_principal = models.TextField(blank=True)
    protocolos_suportados = models.CharField(max_length=100)  # ex: HTTP, HTTPS
    capacidades_dados = models.CharField(max_length=100)  # ex: JSON, XML
    contato_responsavel = models.CharField(max_length=100)
    requisitos_autenticacao = models.CharField(max_length=50)
    session_user_key = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nome


class Interface(models.Model):
    sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE, related_name='interfaces')
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)  # REST API, SOAP, DB, etc
    endpoint = models.TextField()
    formato_dados = models.CharField(max_length=20)  # JSON, XML, etc
    metodos_permitidos = models.CharField(max_length=100, blank=True)
    autenticacao = models.CharField(max_length=50, blank=True)
    operacoes_suportadas = models.TextField(blank=True)
    exemplo_dados = models.TextField(blank=True)
    esquema = models.TextField(blank=True)  # JSON Schema ou XSD
    throttling = models.TextField(blank=True)  # descrição livre

    def __str__(self):
        return f"{self.nome} ({self.sistema.nome})"


class EstiloIntegracao(models.Model):
    sistema_origem = models.ForeignKey(Sistema, on_delete=models.CASCADE, related_name='integracoes_origem')
    sistema_destino = models.ForeignKey(Sistema, on_delete=models.CASCADE, related_name='integracoes_destino')
    estilo = models.CharField(max_length=50)  # Banco Compartilhado, RPC, Mensageria, Arquivo
    detalhes = models.JSONField(blank=True, null=True)  # Armazena os campos específicos em JSON

    def __str__(self):
        return f"{self.estilo} - {self.sistema_origem.nome} → {self.sistema_destino.nome}"
