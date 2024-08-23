from django.db import models
from multiselectfield import MultiSelectField
#Modelo de inspectores

SECCION = (
    ("","Seleccione una Sección"),
    ("INICIAL","INICIAL"),
    ("BASICA","BASICA"),
    ("BASICA ELEMENTAL","BASICA ELEMENTAL"),
    ("BASICA SUPERIOR","BASICA SUPERIOR"),
    ("BACHILLERATO","BACHILLERATO"),
)

class Inspector(models.Model):
    cedula_insp = models.CharField(primary_key = True ,max_length=50)
    nombre_insp = models.CharField(max_length = 100)
    apellido_insp = models.CharField(max_length=100)
    seccion = models.CharField(choices = SECCION, max_length=50,default = 'Ninguna')
    activo = models.BooleanField(default = True)
    fecha_audit = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.nombre_insp}  {self.apellido_insp}'    

#ModeloCurso
JORNADA=(
    ('Matutina','Matutina'),
    ('Vespertina','Vespertina')
    
)
#ModeloDocente
class Docente(models.Model):
    cedula_docente = models.CharField(primary_key = True ,max_length=50)
    nombre_docente = models.CharField(max_length = 100)
    apellido_docente = models.CharField(max_length=100)
    jornada = models.CharField(choices = JORNADA, max_length=50,default = 'Ninguna')
    activo = models.BooleanField(default = True)
    fecha_audit = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.nombre_docente}  {self.apellido_docente}'    

PARALELO = (
('A','A'),
('B','B'),
('C','C'),
('D','D')      
)
    

class Curso(models.Model):
    curso = models.CharField(max_length=50)
    jornada = models.CharField(max_length=15,choices= JORNADA) #V O M CON SELECCION
    paralelo = models.CharField(max_length=50,choices = PARALELO,default = ('A','A'))
    fecha_audit = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.curso}  {self.paralelo}'
    
#Modelo de Estudiantes
class Estudiante(models.Model):
    cedula_est = models.CharField(primary_key = True, max_length=50)
    nombre_est = models.CharField(max_length = 100)
    apellido_est = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True, blank=True)
    activo = models.BooleanField(default = True)
    fecha_audit = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.apellido_est}  {self.nombre_est}'

class Insidencia(models.Model):
    nombre = models.CharField(max_length=500)
    activo = models.BooleanField(default = 1)
    fecha_audit = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre
    
    
class Periodo(models.Model):
    cod_periodo = models.CharField(primary_key = True, max_length=50)
    nombre = models.CharField(max_length=50)
    activo = models.BooleanField(default = True)
    fecha_audit = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.cod_periodo
    
      
class RegistroFaltas(models.Model):

    
    cedula_estudiante = models.ForeignKey(Estudiante, verbose_name=("Estudiantes"), on_delete=models.DO_NOTHING)
    cedula_inspector = models.ForeignKey(Inspector, verbose_name=("Inspectores"), on_delete=models.DO_NOTHING)
    cedula_docente = models.ForeignKey(Docente, verbose_name=("Docentes"), on_delete=models.DO_NOTHING)   
    fecha = models.DateField()
    periodo = models.ForeignKey(Periodo, on_delete=models.DO_NOTHING)
    estado = models.BooleanField(default = True)
    #detalle
    insidencias = models.ManyToManyField(Insidencia,through='RegistroFaltasIncidencia')
    fecha_audit = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Registro de faltas para {self.cedula_estudiante}'
        
    class Meta:
        verbose_name_plural = "Registros de Faltas"

    
class RegistroFaltasIncidencia(models.Model):
    registro_faltas = models.ForeignKey(RegistroFaltas, on_delete=models.CASCADE)
    incidencia = models.ForeignKey(Insidencia, on_delete=models.CASCADE)
    

#ModeloCursoEstudiantes
class EstudiantesCursos(models.Model):
    ced_estudiante = models.ForeignKey(Estudiante, verbose_name=("Estudiantes"), on_delete=models.DO_NOTHING)
    cod_curso = models.ForeignKey(Curso, verbose_name=("Cursos"), on_delete=models.DO_NOTHING)
    cod_seccion = models.CharField(choices = SECCION, max_length=50,default = 'Ninguna')
    cod_periodo = models.ForeignKey(Periodo, verbose_name=("Periodos"), on_delete=models.DO_NOTHING)
    #Audit
    fecha_audit = models.DateTimeField(auto_now_add=True)
    



    
