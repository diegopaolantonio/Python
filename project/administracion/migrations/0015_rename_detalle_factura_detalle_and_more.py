# Generated by Django 5.0.6 on 2024-06-05 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0014_alter_factura_proyecto'),
        ('proyectos', '0003_proyecto_cliente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='factura',
            old_name='Detalle',
            new_name='detalle',
        ),
        migrations.RenameField(
            model_name='factura',
            old_name='FechaEmision',
            new_name='fechaEmision',
        ),
        migrations.RenameField(
            model_name='factura',
            old_name='FechaVencimiento',
            new_name='fechaVencimiento',
        ),
        migrations.RenameField(
            model_name='factura',
            old_name='Moneda',
            new_name='moneda',
        ),
        migrations.RenameField(
            model_name='factura',
            old_name='Monto',
            new_name='monto',
        ),
        migrations.RenameField(
            model_name='factura',
            old_name='Numero',
            new_name='numero',
        ),
        migrations.RenameField(
            model_name='gasto',
            old_name='Detalle',
            new_name='detalle',
        ),
        migrations.RenameField(
            model_name='gasto',
            old_name='FechaEmision',
            new_name='fechaEmision',
        ),
        migrations.RenameField(
            model_name='gasto',
            old_name='FechaVencimiento',
            new_name='fechaVencimiento',
        ),
        migrations.RenameField(
            model_name='gasto',
            old_name='Monto',
            new_name='monto',
        ),
        migrations.RenameField(
            model_name='gasto',
            old_name='Referencia',
            new_name='referencia',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='Proyecto',
        ),
        migrations.RemoveField(
            model_name='gasto',
            name='Moneda',
        ),
        migrations.AddField(
            model_name='factura',
            name='proyecto',
            field=models.ManyToManyField(blank=True, to='proyectos.proyecto'),
        ),
        migrations.AddField(
            model_name='gasto',
            name='moneda',
            field=models.CharField(default='USD', max_length=10),
        ),
    ]
