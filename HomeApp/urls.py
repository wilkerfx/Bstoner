from django.urls import path
from .views import home, entrada_toner, saida_toner, listagem_tudo, botao_add_toner, botao_cancelar_toner, \
    botao_ver_tudo, relatorio, botao_relatorio, botao_add_saida, form_saida_toner


urlpatterns = [
    path('', home, name='index'),
    path('entrada/', entrada_toner, name='entrada'),
    path('saida/', form_saida_toner, name='saida'),
    path('addtoner/', botao_add_toner, name='addtoner'),
    path('add_saida/', botao_add_saida, name='add_saida'),
    path('canceltoner/', botao_cancelar_toner, name='canceltoner'),
    path('vertudo/', botao_ver_tudo, name='viewtudo'),
    path('botao_relatorio/', botao_relatorio, name='botao_relatorio'),
    path('listagem/', listagem_tudo, name='listagem'),
    path('relatorio/', relatorio, name='relatorio'),

]
