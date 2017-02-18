from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Project
from UMLPythonExtractorv2 import proyect

def index(request):
    return render(request, 'pyumlclass/index.html', {})

def archive(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'pyumlclass/archive.html',context)

def results(request):
    results_proyect = proyect.Analyze(request.POST['project_url'])
    print results_proyect
    response = "You'll see the result of this project: " + request.POST['project_url']
    response += "\n"
    return HttpResponse(response)
    # Falta: Una vez recibida la request, comprobar la base de datos, a ver si se ha analizado ese proyecto
    # Si se ha analizado se muestra sin llamar al resto del codigo, si no se llama
    # Hay que comprobar el objeto que se obtiene con la lista
    # Crear plantilla de resultado para un unico proyecto
