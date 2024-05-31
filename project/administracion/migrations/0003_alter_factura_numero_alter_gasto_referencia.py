# Generated by Django 5.0.4 on 2024-05-23 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0002_gasto_delete_gastos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='Numero',
            field=models.DecimalField(decimal_places=0, max_digits=20, unique=True),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='Referencia',
            field=models.CharField(max_length=50),
        ),
    ]