# Generated by Django 5.0.1 on 2024-02-03 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Cpf', models.CharField(max_length=100)),
                ('Nome', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Senha', models.CharField(max_length=100)),
                ('Crm', models.CharField(max_length=100)),
                ('Rg', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Medico',
            },
        ),
    ]
