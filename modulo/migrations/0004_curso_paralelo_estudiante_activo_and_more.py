# Generated by Django 5.0 on 2024-01-19 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo', '0003_remove_registrofaltasincidencia_cedula_estudiante'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='paralelo',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default=('A', 'A'), max_length=50),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='insidencia',
            name='activo',
            field=models.BooleanField(default=1),
        ),
    ]
