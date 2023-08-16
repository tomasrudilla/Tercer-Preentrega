from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('medicos/', medicos, name="medicos"),
    path('pacientes/', pacientes, name="pacientes"),
    path('turnos/', turnos, name="turnos"),
    
    path('medico_form/', medicoForm, name="medico_form"),
    path('medico_form2/', medicoForm2, name="medico_form2"),
    path('paciente_form/', pacienteForm, name="paciente_form"),
    path('paciente_form2/', pacienteForm2, name="paciente_form2"),
    path('turno_form/', turnoForm, name="turno_form"),
    path('turno_form2/', turnoForm2, name="turno_form2"),

    
    
    path('buscar_medico/', buscarMedico, name="buscar_medico"),
    path('buscar2/', buscar2, name="buscar2"),


]