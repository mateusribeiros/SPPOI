from django.urls import path
from .views import rootPage, system

urlpatterns = [
    path('', rootPage.index, name='index'),

    # Caminhos para registro dos sistemas
    path('lab/', system.render_lab, name='render_lab'),

    # path('lab/project/', , name='project'),
    
    path('lab/system/register/', system.register, name='register_system'),
    path('lab/system/save/', system.save, name='save_system'),
    path('lab/system/update/', system.update, name='update_system'),
    path('lab/system/delete/', system.delete, name="delete_system"),

    # path('lab/interface/register/', , name='register_interface'),
    # path('lab/interface/register/save/', , name='save_interface'),
    # path('lab/interface/update/', , name='update_interface'),
    # path('lab/interface/delete/', , name="delete_interface"),

    # path('store/', rootPage.render_save_page, name='render_save_page'),
    # path('api/store/', cache.save_temp_data, name='save_temp_data'),
    # path('retrieve/', cache.get_temp_data, name='get_temp_data'),
]

# Salvar
# Atualizar/Update
# Deletar