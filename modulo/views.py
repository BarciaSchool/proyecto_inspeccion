from django.shortcuts import render, redirect, get_object_or_404
from .forms import InspectorForm,RegistroFaltasForm,EstudianteForm,CursoForm
from .models import RegistroFaltas,Estudiante,Inspector,RegistroFaltasIncidencia
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.http import JsonResponse
from django.views import View
from django.urls import reverse

def curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,"Registro de Curso Completo")
            return HttpResponseRedirect("estudiante")
    else:
        form = CursoForm()
    context= {
          "form":form
          }
    return render(request,'reg_curso.html',context)

def estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,"Registro de estudiante completo.")
            return HttpResponseRedirect('/estudiante')
    else:
        form = EstudianteForm()
    context= {
      "form":form
      }
    return render(request,'reg_estudiante.html',context)

def inspector(request):
    if request.method == 'POST':
        form = InspectorForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,"Registro de inspector completo.")
            return HttpResponseRedirect('/inspector')
    else:
        form = InspectorForm()
    context= {
        "form":form
        }
    return render(request,'reg_inspector.html',context)


def home(request):
    return render(request, 'home.html')

def registrar_faltas(request):
    if request.method == "POST":
        form = RegistroFaltasForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            registro_faltas = form.save(commit=False)
            registro_faltas.save()
            
            incidencias_ids = request.POST.getlist('incidencias')
            for incidencia_id in incidencias_ids:
                RegistroFaltasIncidencia.objects.create(
                    registro_faltas=registro_faltas,
                    incidencia_id=incidencia_id,
                )
            form.save_m2m()

            messages.success(request, "Registro guardado exitosamente.")
            return HttpResponseRedirect('/incidencias/registro')
    else:
        form = RegistroFaltasForm()

    return render(request, "faltas.html", {'form': form})

def editar_registro_faltas(request, id_registro):
    registro = get_object_or_404(RegistroFaltas, id=id_registro)
    seccion = registro.cedula_inspector.seccion

    if request.method == "POST":
        form = RegistroFaltasForm(request.POST, instance=registro)
        if form.is_valid():
            registro_faltas = form.save(commit=False)
            registro_faltas.save()

            # Limpiar las asociaciones anteriores
            registro_faltas.incidencia.clear()

            # Obtener las nuevas asociaciones desde el formulario
            incidencias_seleccionadas = form.cleaned_data['incidencia']
            incidencias_ids = [incidencia.id for incidencia in incidencias_seleccionadas]
            print(incidencias_ids)
            
            # Crear las nuevas asociaciones
            for incidencia_id in incidencias_ids:
                RegistroFaltasIncidencia.objects.create(
                    registro_faltas=registro_faltas,
                    incidencia_id=incidencia_id,
                )

            messages.success(request, "Registro actualizado exitosamente.")
            return HttpResponseRedirect(reverse('editar_registro_faltas', args=[id_registro]))
    else:
        form = RegistroFaltasForm(instance=registro)

    return render(request, "faltas.html", {'form': form , 'seccion':seccion})


def lista_registros(request):
    registros = RegistroFaltas.objects.all()
    return render(request, 'reg_list.html', {'registros': registros})

def detalle_registro(request, registro_id):
    registro = get_object_or_404(RegistroFaltas, pk=registro_id)
    return render(request, 'reg_detalle.html', {'registro': registro})

class ObtenerSeccionView(View):
    def get(self, request, inspector_id):
        try:
            inspector = Inspector.objects.get(pk=inspector_id)
            seccion = inspector.seccion
            return JsonResponse({'seccion': seccion})
        except Inspector.DoesNotExist:
            return JsonResponse({'error': 'Persona no encontrada'}, status=404)
        
def ver_registro_faltas(request, id_registro):
    registro = get_object_or_404(RegistroFaltas, id=id_registro)
    form = RegistroFaltasForm(instance=registro)
    seccion = registro.cedula_inspector.seccion
    readonly = True  # Establecer modo solo lectura

    return render(request, "faltas_readonly.html", {'form': form, 'readonly': readonly, 'seccion': seccion})

def eliminar_registro_faltas(request, id_registro):
    registro = get_object_or_404(RegistroFaltas, id=id_registro)
    seccion = registro.cedula_inspector.seccion
    form = RegistroFaltasForm(instance=registro)
    if request.method == "POST":
        # Si la solicitud es POST, confirmamos y eliminamos el registro
        registro.delete()
        # Redirigimos a alguna página de éxito, o cualquier página que desees
        return redirect('lista_registro')
    # Si no es una solicitud POST, simplemente renderizamos un mensaje de confirmación
    return render(request, "eliminar_registro_faltas.html", {'form': form,'seccion':seccion})

