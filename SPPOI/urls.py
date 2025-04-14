from django.urls import path
from .views import project, rootPage, system, interface

urlpatterns = [
    path('', rootPage.index, name='index'),
    path('lab/', rootPage.render_lab, name='render_lab'),
    
    path('lab/project/<int:id>', project.render_project, name='render_project'),
    path('lab/project/register/', project.register_project, name='register_project'),

    path('lab/project/<int:id>/system/', system.render_system, name='render_system'),
    path('lab/project/<int:id>/system/register/', system.register, name='register_system'),
    # path('lab/project/<int:id>/system/update/', system.update, name='update_system'),
    # path('lab/project/<int:id>/system/delete/', system.delete, name="delete_system"),

    path('lab/project/<int:id>/interface/', interface.render_interface, name='render_interface'),
    path('lab/project/<int:id>/interface/register/', interface.register, name='register_interface'),
    # path('lab/interface/update/', , name='update_interface'),
    # path('lab/interface/delete/', , name="delete_interface"),

    # path('store/', rootPage.render_save_page, name='render_save_page'),
    # path('api/store/', cache.save_temp_data, name='save_temp_data'),
    # path('retrieve/', cache.get_temp_data, name='get_temp_data'),
]

# Salvar
# Atualizar/Update
# Deletar