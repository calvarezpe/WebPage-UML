from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Project
from UMLPythonExtractorv2 import proyect
from django.core.exceptions import ObjectDoesNotExist
import urllib2

def index(request):
    return render(request, 'pyumlclass/index.html', {})

def archive(request):
    projects = Project.objects.all()
    print("Consulta a la base de datos de todos los proyectos")
    context = {'projects': projects}
    return render(request, 'pyumlclass/archive.html',context)

def results(request):
    Page = HttpResponse("Null page")
    url_project_given = request.POST['project_url']
    if(len(url_project_given.split("https://github.com")) == 2):
        project_name_from_url = url_project_given.split("github.com")[-1]
        # Comprobar si existe el proyecto
        try:
            print("API de GitHub para comprobar existencia proyecto")
            request_api_github = "https://api.github.com/repos" + project_name_from_url
            f = urllib2.urlopen(request_api_github)
            try:
                print("Consulta a la BBDD sobre el proyecto")
                q = Project.objects.get(name_text=project_name_from_url)
                # Por aqui sigue si el proyecto se ha analizado
                print("Proyecto existente. Se muestran los resultados.")
                context = {'project':q}
                Page = render(request, 'pyumlclass/one_project.html',context)
            except ObjectDoesNotExist:
                # Por aqui sigue si el proyecto no esta en la base de datos
                print("Proyecto no existente en BBDD. Se analiza el proyecto.")
                results_proyect = proyect.Analyze(url_project_given)

                q = Project(name_text=project_name_from_url,
                            uml_class=results_proyect[0],
                            python_class=results_proyect[1],
                            intersection=results_proyect[2],
                            without_corrections=results_proyect[3],
                            hamming_corrections=results_proyect[4],
                            capital_letters_corrections=results_proyect[5])
                q.save()
                print("Se incluye a la base de datos y se muestran los resultados")
                context = {'project':q}
                Page = render(request, 'pyumlclass/one_project.html',context)
        except urllib2.URLError, e:
            Page = HttpResponse("The project named " + project_name_from_url + " does not exist.")
    else:
        Page = HttpResponse("Link error. Link must be https://github.com/user/project_name")

    return Page
