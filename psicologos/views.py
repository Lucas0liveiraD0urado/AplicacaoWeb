from django.shortcuts import render, get_object_or_404, redirect
from .models import Psicologo, Instituicao, Agendamento
from django.http import HttpResponse

def home(request):
    return render(request, 'psicologos/home.html')

def lista_psicologos(request):
    psicologos = Psicologo.objects.all()
    return render(request, 'psicologos/lista_psicologos.html', {'psicologos': psicologos})

def detalhe_psicologo(request, psicologo_id):
    psicologo = get_object_or_404(Psicologo, pk=psicologo_id)
    return render(request, 'psicologos/detalhe_psicologo.html', {'psicologo': psicologo})

def agendar_atendimento(request, psicologo_id):
    psicologo = get_object_or_404(Psicologo, id=psicologo_id)
    
    if request.method == 'POST':
        cliente_nome = request.POST.get('cliente_nome')
        data = request.POST.get('data')
        idade = request.POST.get('idade') 
        descricao = request.POST.get('descricao')

        if not idade:
            return HttpResponse("A idade é obrigatória.")  

        try:
            idade = int(idade)
        except ValueError:
            return HttpResponse("A idade deve ser um número válido.")  

        agendamento = Agendamento(
            psicologo=psicologo,
            cliente_nome=cliente_nome,
            data=data,
            idade=idade,  
            descricao=descricao
        )
        agendamento.save()
        return redirect('psicologos:lista_psicologos')  

    return render(request, 'psicologos/agendar_atendimento.html', {'psicologo': psicologo})

def instituicao(request):
    instituicao = Instituicao.objects.first()
    psicologos = Psicologo.objects.all()
    return render(request, 'psicologos/instituicao.html', {'instituicao': instituicao, 'psicologos': psicologos})