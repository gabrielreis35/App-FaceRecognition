# Generated by Django 5.0.1 on 2024-04-05 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescricoes', '0002_alter_prescricao_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescricao',
            name='Ativo',
            field=models.BooleanField(default=True),
        ),
    ]