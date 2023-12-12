from django.shortcuts import render
import Analytics
from aplicacion.models import DISPOSITIVOS
from aplicacion.models import Usuario
from aplicacion.models import registroDispositivos
from aplicacion.models import Informe
def index(request):
    dispositivos = DISPOSITIVOS.objects.all()
    usuario = Usuario.objects.all()
    return render(request, 'index.html', {'usuario': usuario})

def RegistroDeDispositivos(request):
    dispositivos = DISPOSITIVOS.objects.all()
    return render(request, 'RegistroDeDispositivos.html', {'dispositivos':dispositivos})

def FormularioDeDispositivos(request):
    registro = registroDispositivos.objects.all()
    return render(request, 'Registro', {'registro': registro})

def GenerarInforme(request):
    informe = Informe.objects.all()
    return render(request, {'informe':informe})
# Create your views here.

