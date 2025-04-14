from django.contrib import admin
from .models import Projeto, Sistema, Interface, EstiloIntegracao


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Projeto._meta.fields]
    search_fields = ('nome', 'criado_em', 'session_key')
    list_filter = ('nome', 'criado_em', 'session_key')

@admin.register(Sistema)
class SistemaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Sistema._meta.fields]
    search_fields = ('nome', 'tipo', 'versao', 'contato_responsavel')
    list_filter = ('tipo', 'versao')

@admin.register(Interface)
class InterfaceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Interface._meta.fields]
    search_fields = ('nome', 'tipo', 'sistema__nome', 'formato_dados')
    list_filter = ('tipo', 'formato_dados')

@admin.register(EstiloIntegracao)
class EstiloIntegracaoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EstiloIntegracao._meta.fields]
    search_fields = ('estilo', 'sistema_origem__nome', 'sistema_destino__nome', 'projeto')
    list_filter = ('estilo', 'projeto')
