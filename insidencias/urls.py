"""
URL configuration for insidencias project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from modulo.views import inspector,curso,estudiante,registrar_faltas,lista_registros,ObtenerSeccionView,home,editar_registro_faltas,ver_registro_faltas,eliminar_registro_faltas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('incidencias/registro', registrar_faltas, name='registro_faltas'),
    path('incidencias/update/<int:id_registro>/', editar_registro_faltas, name='editar_registro_faltas'),
    path('', home, name='home'),
    path('estudiante/', estudiante, name='registro_estudiante'),
    path('incidencias/list', lista_registros, name='lista_registro'),
    path('cursos/', curso, name='registro_curso'),
    path('inspector/', inspector, name='registro_inspector'),
    #Otras Urls
    path("select2/", include("django_select2.urls")),
    path('obtener_seccion/<str:inspector_id>/', ObtenerSeccionView.as_view(), name='obtener_seccion'),
    path('incidencias/list/<str:id_registro>/', ver_registro_faltas, name='ver_registro_faltas'),
    path('incidencias/list/delete/<str:id_registro>', eliminar_registro_faltas, name='eliminar_registro'),
    path('account/',include('account.urls')),
    
]

