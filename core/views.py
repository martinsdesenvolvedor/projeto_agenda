from django.shortcuts import render
from core.models import Evento

# Create your views here.
'''def lista_eventos(request):
    return render(request, 'agenda.html')'''

'''def lista_eventos(request):
    evento = Evento.objects.get(id=2)
    dados = {'evento': evento}
    return render(request, 'agenda.html', dados)'''

'''def lista_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)'''

def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)