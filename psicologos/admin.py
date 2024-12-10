from django.contrib import admin
from .models import Psicologo, Agendamento, Instituicao

admin.site.register(Psicologo)

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('cliente_nome', 'psicologo', 'data', 'idade', 'descricao')  
    search_fields = ('cliente_nome', 'psicologo__nome') 
    list_filter = ('psicologo', 'data') 