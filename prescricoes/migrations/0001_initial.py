# Generated by Django 5.0.1 on 2024-04-08 17:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0002_alter_userprofile_reconhecimentofacial'),
        ('medicamentos', '0001_initial'),
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Data', models.DateTimeField(auto_now_add=True)),
                ('Ativo', models.BooleanField(default=True)),
                ('Medicamentos', models.ManyToManyField(to='medicamentos.medicamento')),
                ('Medico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='login.userprofile')),
                ('Paciente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pacientes.paciente')),
            ],
            options={
                'db_table': 'Prescricao',
            },
        ),
    ]
