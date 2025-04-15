from django.urls import path
from .views import project, rootPage, system, interface, integration

urlpatterns = [
    # Página inicial e laboratório
    path('', rootPage.index, name='index'),
    path('lab/', rootPage.render_lab, name='render_lab'),

    # Projeto
    path('lab/project/<int:id>/', project.render_project, name='render_project'),
    path('lab/project/register/', project.register_project, name='register_project'),
    path('lab/project/<int:id>/delete/', project.delete, name='delete_project'),

    # Sistema
    path('lab/project/<int:id>/system/', system.render_system, name='render_system'),
    path('lab/project/<int:id>/system/register/', system.register, name='register_system'),
    # path('lab/project/<int:id>/system/update/', system.update, name='update_system'), 
    path('lab/project/<int:id>/system/delete/<int:idSystem>/', system.delete, name='delete_system'),

    # Interface
    path('lab/project/<int:id>/interface/', interface.render_interface, name='render_interface'),
    path('lab/project/<int:id>/interface/register/', interface.register, name='register_interface'),
    # path('lab/interface/update/', interface.update, name='update_interface'),
    path('lab/project/<int:id>/interface/delete/<int:idInterface>/', interface.delete, name='delete_interface'),

    # Estilo de Integração
    path('lab/project/<int:id>/integration/', integration.render_integration, name='render_integration'),
    path('lab/project/<int:id>/integration/register/', integration.register, name='register_integration'),
    path('lab/project/<int:id>/integration/delete/<int:idIntegration>/', integration.delete, name='delete_integration'),
    path('lab/project/<int:id>/integration/update/<int:idIntegration>/', integration.update, name='update_integration'),
    path('lab/project/<int:id>/integration/updateData/<int:idIntegration>/', integration.updateData, name='update_integrationData'),

    # Futuras rotas para salvar dados temporários
    # path('store/', rootPage.render_save_page, name='render_save_page'),
    # path('api/store/', cache.save_temp_data, name='save_temp_data'),
    # path('retrieve/', cache.get_temp_data, name='get_temp_data'),
]
