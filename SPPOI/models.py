from django.db import models


class Projeto(models.Model):
    nome = models.CharField(max_length=100, default="Projeto Temporário")
    criado_em = models.DateTimeField(auto_now_add=True)
    session_key = models.CharField(max_length=100, null=False, blank=False, db_index=True)


    def __str__(self):
        return f"Projeto {self.nome} - {self.session_key}"

class Sistema(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='sistemas')
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    tipo = models.CharField(max_length=50)
    versao = models.CharField(max_length=20)
    funcionalidade_principal = models.TextField(blank=True)
    protocolos_suportados = models.CharField(max_length=100) 
    capacidades_dados = models.CharField(max_length=100)
    email_responsavel = models.CharField(max_length=100, blank=True)
    contato_responsavel = models.CharField(max_length=100, blank=True)
    mantenedor = models.CharField(max_length=100, blank=True)
    requisitos_autenticacao = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Interface(models.Model):
    sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE, related_name='interfaces')
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='interfaces_projeto')
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    endpoint = models.TextField()
    formato_dados = models.CharField(max_length=20)  
    metodos_permitidos = models.CharField(max_length=100, blank=True)
    autenticacao = models.CharField(max_length=50, blank=True)
    operacoes_suportadas = models.TextField(blank=True)
    exemplo_dados = models.TextField(blank=True)
    esquema = models.TextField(blank=True) 
    throttling = models.TextField(blank=True) 

    def __str__(self):
        return f"{self.nome} ({self.sistema.nome})"


class EstiloIntegracao(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='estilos_integracao')
    sistema_origem = models.ForeignKey(Sistema, on_delete=models.CASCADE, related_name='integracoes_origem')
    sistema_destino = models.ForeignKey(Sistema, on_delete=models.CASCADE, related_name='integracoes_destino')
    estilo = models.CharField(max_length=50)  
    detalhes = models.JSONField(blank=True, null=True) 

    def __str__(self):
        return f"{self.estilo} - {self.sistema_origem.nome} → {self.sistema_destino.nome}"
