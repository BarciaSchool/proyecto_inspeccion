from django import forms
from django.contrib import admin
from .models import Insidencia, RegistroFaltas, Estudiante, Curso, Inspector, RegistroFaltasIncidencia,Periodo,Docente


class RegistroFaltasIncidenciaInline(admin.TabularInline):
    model = RegistroFaltasIncidencia
    extra = 1 

@admin.register(Insidencia)
class InsidenciaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'activo')

@admin.register(RegistroFaltas)
class RegistroFaltasAdmin(admin.ModelAdmin):
    list_display = ('cedula_estudiante', 'cedula_inspector', 'fecha', 'periodo', 'estado')
    inlines = [RegistroFaltasIncidenciaInline]

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('cedula_est', 'nombre_est', 'apellido_est', 'curso')

@admin.register(Inspector)
class InspectorAdmin(admin.ModelAdmin):
    list_display = ('cedula_insp', 'nombre_insp', 'apellido_insp','seccion')   

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('cedula_docente', 'nombre_docente', 'apellido_docente','jornada','activo')   

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('curso','paralelo','jornada')
    
@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('cod_periodo', 'nombre','activo')
    

