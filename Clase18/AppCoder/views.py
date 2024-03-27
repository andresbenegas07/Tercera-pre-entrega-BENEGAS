#from curses import nocbreak
from django.shortcuts import render
from AppCoder.models import Curso
from AppCoder.models import Alumno
from AppCoder.models import Profesor 
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario
from AppCoder.forms import Alumno_formulario 
from AppCoder.forms import Profesor_formulario  




def inicio(request):
    return render(request, "padre.html")



def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


def ver_profesor(request):
    profesor = Profesor.objects.all()
    dicc = {"profesor": profesor}
    plantilla = loader.get_template("profesor.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def ver_alumno(request):
    alumno = Alumno.objects.all()
    dicc = {"alumno": alumno}
    plantilla = loader.get_template("alumnos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)




def curso_formulario(request):
    
    if request.method == "POST":

        mi_formulario = Curso_formulario(request.POST)

        if mi_formulario.is_valid():
           datos = mi_formulario.cleaned_data 
           curso = Curso(nombre=datos["nombre"], camada=datos["camada"])
           curso.save()
           return render(request, "formulario.html")
    
    
    return render(request, "formulario.html")



def alumnos(request):
    return render(request,"alumnos.html")

def alumno_formulario(request):
    
    if request.method == "POST":

        mi_formulario_alumno = Alumno_formulario(request.POST)

        if mi_formulario_alumno.is_valid():
           datos = mi_formulario_alumno.cleaned_data 
           alumno = Alumno(nombre=datos["nombre"], camada=datos["camada"])
           alumno.save()
           return render(request, "alumno_form.html")
    
    
    return render(request, "alumno_form.html") 





def profesor(request):
    return render(request,"profesor.html")

def profesor_formulario(request):
    
    if request.method == "POST":

        mi_formulario_profesor = Profesor_formulario(request.POST)

        if mi_formulario_profesor.is_valid():
           datos = mi_formulario_profesor.cleaned_data 
           profesor = Profesor(nombre=datos["nombre"], camada=datos["camada"])
           profesor.save()
           return render(request, "profesor_form.html")
    
    
    return render(request, "profesor_form.html") 






def buscar_curso(request):

    return render(request, "buscar_curso.html")



def buscar(request):
     
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains= nombre)
        return render(request,"resultado_busqueda.html", {"cursos":cursos})
    else:    
        return HttpResponse("Ingrese el nombre del curso")




def buscar_alumno_r(request):

    return render(request, "buscar_alumno_r.html")


def buscar_alumno(request):
     
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        alumno = Alumno.objects.filter(nombre__icontains= nombre)
        return render(request,"resultado_busqueda_alumno.html", {"alumno":alumno})
    else:    
        return HttpResponse("Ingrese el nombre del alumno")    