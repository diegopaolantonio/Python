# Generated by Django 5.0.6 on 2024-06-05 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0006_rename_pais_area_sede_alter_personal_apellido_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personal',
            old_name='Apellido',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='personal',
            old_name='Area_id',
            new_name='area_id',
        ),
        migrations.RenameField(
            model_name='personal',
            old_name='Avatar',
            new_name='avatar',
        ),
        migrations.RenameField(
            model_name='personal',
            old_name='DNI',
            new_name='dni',
        ),
        migrations.RenameField(
            model_name='personal',
            old_name='Nombre',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='personal',
            old_name='Usuario',
            new_name='usuario',
        ),
    ]
