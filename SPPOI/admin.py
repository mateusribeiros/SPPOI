from django.contrib import admin
from .models import Sistema, Interface, EstiloIntegracao

@admin.register(Sistema)
class SistemaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'versao', 'contato_responsavel')
    search_fields = ('nome', 'tipo', 'versao', 'contato_responsavel')
    list_filter = ('tipo', 'versao')

@admin.register(Interface)
class InterfaceAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'sistema', 'formato_dados')
    search_fields = ('nome', 'tipo', 'sistema__nome', 'formato_dados')
    list_filter = ('tipo', 'formato_dados')

@admin.register(EstiloIntegracao)
class EstiloIntegracaoAdmin(admin.ModelAdmin):
    list_display = ('estilo', 'sistema_origem', 'sistema_destino')
    search_fields = ('estilo', 'sistema_origem__nome', 'sistema_destino__nome')
    list_filter = ('estilo',)
