# Generated by Django 5.0.6 on 2024-05-31 23:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0003_alter_factura_numero_alter_gasto_referencia'),
        ('proyectos', '0003_proyecto_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='Cliente',
        ),
        migrations.AlterField(
            model_name='factura',
            name='Proyecto',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='factura_proyecto', to='proyectos.proyecto'),
        ),
    ]
