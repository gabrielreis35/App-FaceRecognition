# Generated by Django 5.0.1 on 2024-04-08 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cpf', models.CharField(max_length=100)),
                ('Nome', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Rg', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Paciente',
            },
        ),
    ]
