# Generated by Django 5.0.6 on 2024-06-01 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0008_proyecto_factura_alter_factura_proyecto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proyecto_factura',
            old_name='Proyecto',
            new_name='Proyecto_facturado',
        ),
    ]
