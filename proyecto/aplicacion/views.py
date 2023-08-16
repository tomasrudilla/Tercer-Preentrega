from django.shortcuts import render
from .models import Medico, Paciente, Turno
from django.http import HttpResponse
from .forms import MedicoForm
from .forms import PacienteForm
from .forms import TurnoForm

# Create your views here.
def home (request):
    return render(request, "aplicacion/home.html")



def medicos (request):
    contexto = {'medicos' : Medico.objects.all(), 'titulo' : 'Reporte de Medicos', 'grupos' : ['32332' , '87687']}
    return render(request, "aplicacion/medicos.html", contexto)

def pacientes (request):
    contexto = {'pacientes' : Paciente.objects.all()}
    return render(request, "aplicacion/pacientes.html" , contexto)

def turnos (request):
    contexto = {'turnos' : Turno.objects.all()}
    return render(request, "aplicacion/turnos.html" , contexto)


def medicoForm(request):
    if request.method == "POST":
        medico = Medico(nombre=request.POST['nombre'],
                        dni=request.POST['dni'])
        medico.save()
        return HttpResponse("Se grabo con exito el medico!")
    return render(request, "aplicacion/medicoForm.html")


def medicoForm2(request):
    if request.method == "POST":
        miForm = MedicoForm(request.POST)
        if miForm.is_valid():
            medico_nombre = miForm.cleaned_data.get('nombre')
            medico_dni = miForm.cleaned_data.get('dni')
            medico = Medico(nombre=medico_nombre , dni = medico_dni)
            medico.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = MedicoForm()
    
    return render(request, "aplicacion/medicoForm2.html", {"form" : miForm})



def buscarMedico(request):
    return render(request,"aplicacion/buscarMedico.html")

def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        medicos = Medico.objects.filter(nombre__icontains=patron)
        contexto = {"medicos" : medicos,'titulo' : f'Reporte de Medicos que tiene "{patron}"'}
        return render(request, "aplicacion/medicos.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")

def pacienteForm(request):
    if request.method == "POST":
        paciente = Paciente(nombre=request.POST['nombre'],
                        dni=request.POST['dni'],
                        apellido=request.POST['apellido'])
        
        paciente.save()
        return HttpResponse("Se grabo con exito el paciente!")
    return render(request, "aplicacion/pacienteForm.html")

def pacienteForm2(request):
    if request.method == "POST":
        miForm = PacienteForm(request.POST)
        if miForm.is_valid():
            paciente_nombre = miForm.cleaned_data.get('nombre')
            paciente_apellido = miForm.cleaned_data.get('apellido')
            paciente_dni = miForm.cleaned_data.get('dni')
            paciente = Paciente(nombre = paciente_nombre, dni = paciente_dni, apellido = paciente_apellido )
            paciente.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = PacienteForm()
    
    return render(request, "aplicacion/pacienteForm2.html", {"form" : miForm})

def turnoForm(request):
    if request.method == "POST":
        turno = Turno(nombre=request.POST['nombre'],
                        dni=request.POST['dni'],
                        fecha=request.POST['fecha'])
        turno.save()
        return HttpResponse("Se grabo con exito el turno!")
    return render(request, "aplicacion/turnoForm.html")


def turnoForm2(request):
    if request.method == "POST":
        miForm = TurnoForm(request.POST)
        if miForm.is_valid():
            turno_nombre = miForm.cleaned_data.get('nombre')
            turno_dni = miForm.cleaned_data.get('dni')
            turno_fecha = miForm.cleaned_data.get('fecha')
            turno = Turno(nombre=turno_nombre , dni = turno_dni,  fecha = turno_fecha)
            turno.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = TurnoForm()
    
    return render(request, "aplicacion/turnoForm2.html", {"form" : miForm})
