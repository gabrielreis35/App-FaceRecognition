# Generated by Django 5.0.1 on 2024-04-04 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicamento',
            name='DataRetirada',
        ),
        migrations.AddField(
            model_name='medicamento',
            name='Porta',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]