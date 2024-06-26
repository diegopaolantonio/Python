# Generated by Django 5.0.6 on 2024-05-22 03:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('pais', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'area',
                'verbose_name_plural': 'areas',
            },
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(blank=True, max_length=100, null=True)),
                ('DNI', models.DecimalField(decimal_places=0, max_digits=20, unique=True)),
                ('Area_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='personal.area', verbose_name='Area de trabajo')),
            ],
            options={
                'verbose_name': 'personal',
                'verbose_name_plural': 'personal',
            },
        ),
    ]
