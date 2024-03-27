from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="home"),
    path("ver_cursos",views.ver_cursos, name="cursos"),
    path("alumnos", views.alumnos, name="alumnos"),
    path("buscar_curso", views.buscar_curso),
    path("alta_curso", views.curso_formulario),
    path("buscar", views.buscar),
    path("alta_alumno", views.alumno_formulario),
    path("alta_profesor", views.profesor_formulario),
    path("ver_profesor",views.ver_profesor, name="profesores"),
    path("ver_alumno",views.ver_alumno, name="alumno"),
    path("buscar_alumno", views.buscar_alumno, name="buscar_alumno"),
    path("buscar_alumno_r", views.buscar_alumno_r),


]