from django.urls import path
from .views import lista_psicologos, detalhe_psicologo, agendar_atendimento, instituicao, home

app_name = 'psicologos'

urlpatterns = [
    path('', home, name='home'),
    path('lista/', lista_psicologos, name='lista_psicologos'),
    path('detalhe/<int:psicologo_id>/', detalhe_psicologo, name='detalhe_psicologo'),
    path('instituicao/', instituicao, name='instituicao'),
    path('agendar/<int:psicologo_id>/', agendar_atendimento, name='agendar_atendimento'),
]