# Generated by Django 5.0.1 on 2024-02-03 17:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medicamentos', '0001_initial'),
        ('medicos', '0001_initial'),
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescricao',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Data', models.DateTimeField()),
                ('Quantidade', models.IntegerField()),
                ('IdMedicamento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='medicamentos.medicamento')),
                ('IdMedico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='medicos.medico')),
                ('IdPaciente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pacientes.paciente')),
            ],
            options={
                'db_table': 'Prescricao',
            },
        ),
    ]