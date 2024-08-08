# Generated by Django 5.0 on 2024-04-21 04:21

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo', '0014_alter_registrofaltas_cedula_docente'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='fecha_audit',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='docente',
            name='fecha_audit',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estudiante',
            name='fecha_audit',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='insidencia',
            name='fecha_audit',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inspector',
            name='fecha_audit',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='periodo',
            name='fecha_audit',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registrofaltas',
            name='fecha_audit',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='EstudiantesCursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_seccion', models.CharField(choices=[('', 'Seleccione una Sección'), ('INICIAL', 'INICIAL'), ('BASICA', 'BASICA'), ('BASICA ELEMENTAL', 'BASICA ELEMENTAL'), ('BASICA SUPERIOR', 'BASICA SUPERIOR'), ('BACHILLERATO', 'BACHILLERATO')], default='Ninguna', max_length=50)),
                ('fecha_audit', models.DateTimeField(auto_now_add=True)),
                ('ced_estudiante', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='modulo.estudiante', verbose_name='Estudiantes')),
                ('cod_curso', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='modulo.curso', verbose_name='Cursos')),
                ('cod_periodo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='modulo.periodo', verbose_name='Periodos')),
            ],
        ),
    ]
