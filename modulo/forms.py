from django import forms
from django.forms import SelectDateWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div,HTML
from .models import RegistroFaltas, Incidencia,Estudiante,Inspector,Curso,Periodo,Docente
from django.core.validators import RegexValidator
from django_select2.forms import Select2Widget


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['cedula_est', 'nombre_est', 'apellido_est', 'curso']

    cedula_est = forms.CharField(
        label='Cédula del Estudiante',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={'unique': 'El estudiante que intentas registrar ya existe.',
                        'required': 'Por favor, escriba una cédula.'},
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message='La cédula debe contener exactamente 10 dígitos.',
                code='invalid_cedula'
            )
        ]
    )

    nombre_est = forms.CharField(
        label='Nombre del Estudiante',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z\s]+$',
                message='Ingrese un nombre válido (solo letras y espacios).',
                code='invalid_nombre'
            )
        ]
    )

    apellido_est = forms.CharField(
        label='Apellido del Estudiante',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z\s]+$',
                message='Ingrese un apellido válido (solo letras y espacios).',
                code='invalid_apellido'
            )
        ]
    )

    curso = forms.ModelChoiceField(
        label='Curso',
        queryset=Curso.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    
    
class DocenteForm(forms.ModelForm):
    class Meta:
        model= Docente
        fields =  ['cedula_docente','nombre_docente','apellido_docente','jornada']
        
    cedula_docente = forms.CharField(
        label='Cédula del docente',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message='La cédula debe contener exactamente 10 dígitos.',
                code='invalid_cedula'
            )
        ]
    )

    nombre_docente = forms.CharField(
        label='Nombre del docente',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z\s]+$',
                message='Ingrese un nombre válido (solo letras y espacios).',
                code='invalid_nombre'
            )
        ]
    )

    apellido_docente = forms.CharField(
        label='Apellido del docente',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z\s]+$',
                message='Ingrese un apellido válido (solo letras y espacios).',
                code='invalid_apellido'
            )
        ]
    )
    
    JORNADA=(
        ('Selecciona una Jornada',''),
        ('Matutina','Matutina'),
        ('Vespertina','Vespertina')
    )
    jornada = forms.ChoiceField(
        label='Jornada',
        choices= JORNADA,
        widget=forms.Select(attrs={'class': 'form-control'}) 
    )
           
class InspectorForm(forms.ModelForm):
    class Meta:
        model= Inspector
        fields =  ['cedula_insp','nombre_insp','apellido_insp','seccion']
        
    cedula_insp = forms.CharField(
        label='Cédula del Inspector',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message='La cédula debe contener exactamente 10 dígitos.',
                code='invalid_cedula'
            )
        ]
    )

    nombre_insp = forms.CharField(
        label='Nombre del Inspector',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z\s]+$',
                message='Ingrese un nombre válido (solo letras y espacios).',
                code='invalid_nombre'
            )
        ]
    )

    apellido_insp = forms.CharField(
        label='Apellido del Inspector',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z\s]+$',
                message='Ingrese un apellido válido (solo letras y espacios).',
                code='invalid_apellido'
            )
        ]
    )
    
    SECCION = (
    ("","Seleccione una Sección"),
    ("INICIAL","INICIAL"),
    ("BASICA","BASICA"),
    ("BASICA ELEMENTAL","BASICA ELEMENTAL"),
    ("BASICA SUPERIOR","BASICA SUPERIOR"),
    ("BACHILLERATO","BACHILLERATO"),
        )
    seccion = forms.ChoiceField(
        label='Sección',
        choices= SECCION,
        widget=forms.Select(attrs={'class': 'form-control'}) 
    )
    
   
        
        
        
class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields  = ['curso','jornada','paralelo']

class RegistroFaltasForm(forms.ModelForm):
    class Meta:
        model = RegistroFaltas
        fields = ['cedula_estudiante', 'cedula_inspector','cedula_docente', 'fecha', 'periodo', 'incidencias']
        
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={'readonly': 'readonly'}),
        error_messages={'required': 'Por favor, selecciona una fecha.'}
    )
    
    cedula_estudiante = forms.ModelChoiceField(
        queryset=Estudiante.objects.filter(activo=True),
        empty_label='Seleciona un Estudiante',
        error_messages={'required': 'Por favor, selecciona un Estudiante.'},
        widget= forms.Select,
    )
    
    cedula_docente = forms.ModelChoiceField(
        queryset=Docente.objects.filter(activo=True),
        empty_label='Seleciona el docente reportador',
        error_messages={'required': 'Por favor, selecciona un Docente.'},
        widget= forms.Select,
    )
    cedula_inspector = forms.ModelChoiceField(
        queryset=Inspector.objects.filter(activo=True),
        empty_label='Seleciona un Inspector',
        error_messages={'required': 'Por favor, selecciona un Inspector.'},
        widget= forms.Select,
    )
    
    periodo = forms.ModelChoiceField(
        queryset=Periodo.objects.filter(activo=True),
        empty_label='Seleciona un periodo',
        error_messages={'required': 'Por favor, selecciona un periodo.'},
        widget= forms.Select,
    )
    
    seccion = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'disabled': 'disabled'}),
        required=False
    )
    
    incidencias = forms.ModelMultipleChoiceField(
        label='Incidencias',
        queryset=Incidencia.objects.filter(activo=True),
        error_messages={'required': 'Por favor, selecciona al menos una incidencia.'},
        widget=forms.CheckboxSelectMultiple
    )
    
    def set_estudiantes_choices(self):
        # Consulta a la base de datos para obtener las opciones de cedula_estudiante
        estudiantes = Estudiante.objects.all()
        choices = [(estudiante.cedula_est, f'{estudiante.apellido_est} {estudiante.nombre_est}') for estudiante in estudiantes]
        self.fields['cedula_estudiante'].choices = [('','Selecion un estudiante')] + choices
        
    def set_inspectores_choices(self):
        # Consulta a la base de datos para obtener las opciones de cedula_estudiante
        inspectores = Inspector.objects.filter(activo=True)
        choices = [(inspector.cedula_insp, f'{inspector.apellido_insp} {inspector.nombre_insp}') for inspector in inspectores]
        self.fields['cedula_inspector'].choices = [('','Selecion un Inspector')] + choices
        
    def set_docentes_choices(self):
        # Consulta a la base de datos para obtener las opciones de cedula_estudiante
        docentes = Docente.objects.filter(activo=True)
        choices = [(docente.cedula_docente, f'{docente.apellido_docente} {docente.nombre_docente}') for docente in docentes]
        self.fields['cedula_docente'].choices = [('','Selecion un Docente')] + choices
    
        
    def set_periodos_choices(self):
        # Consulta a la base de datos para obtener las opciones de cedula_estudiante
        periodos = Periodo.objects.filter(activo=True)
        choices = [(periodo.cod_periodo, periodo.cod_periodo) for periodo in periodos]
        self.fields['periodo'].choices = [('','Selecion un periodo')] + choices

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Llama a la función para establecer las opciones del campo cedula_estudiante
        self.set_estudiantes_choices()
        self.set_inspectores_choices()
        self.set_periodos_choices()
        self.set_docentes_choices()

        # Obtener la instancia actual del modelo
        instancia_actual = kwargs.get('instance')

        # Si estamos en el modo de edición y hay una instancia actual
        if instancia_actual and instancia_actual.pk:
            # Obtener las instancias asociadas a través del ManyToManyField
            incidencias_asociadas = instancia_actual.incidencias.all()
            # Preseleccionar las opciones en el campo incidencias
            self.fields['incidencias'].initial = list(incidencias_asociadas.values_list('id', flat=True))

    
        
        



