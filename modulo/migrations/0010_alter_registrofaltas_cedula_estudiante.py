# Generated by Django 5.0 on 2024-01-29 03:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo', '0009_registrofaltas_estado_alter_registrofaltas_periodo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrofaltas',
            name='cedula_estudiante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='modulo.estudiante', verbose_name='Estudiantes'),
        ),
    ]
