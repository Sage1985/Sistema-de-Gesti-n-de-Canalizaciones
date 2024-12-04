from django.shortcuts import render, redirect
from .models import Solicitud, Alumno
from .forms import SolicitudForm
from rest_framework.viewsets import ModelViewSet
from .models import Solicitud
from .serializers import SolicitudSerializer
from .models import Alumno
from django import forms

def listar_solicitudes(request):
    solicitudes = Solicitud.objects.all()
    return render(request, 'canalizaciones/solicitudes.html', {'solicitudes': solicitudes})

class SolicitudViewSet(ModelViewSet):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer

def crear_solicitud(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_solicitudes')
    else:
        form = SolicitudForm()
    return render(request, 'canalizaciones/crear_solicitud.html', {'form': form})

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'grupo', 'matricula']

def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_solicitudes')  
    else:
        form = AlumnoForm()
    return render(request, 'canalizaciones/crear_alumno.html', {'form': form})
