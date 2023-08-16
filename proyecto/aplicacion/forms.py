from django import forms

class MedicoForm(forms.Form):
    nombre  = forms.CharField(max_length=50, required=True)
    dni = forms.IntegerField(required=True)

class PacienteForm(forms.Form):
    nombre  = forms.CharField(max_length=50, required=True)
    dni = forms.IntegerField(required=True)   
    apellido = forms.CharField(max_length=50)

class TurnoForm(forms.Form):
    nombre  = forms.CharField(max_length=50, required=True)
    dni = forms.IntegerField(required=True)   
    fecha = forms.CharField(max_length=50, required=True)