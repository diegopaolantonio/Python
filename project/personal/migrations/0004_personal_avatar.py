# Generated by Django 5.0.6 on 2024-06-03 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_rename_usuario_personal_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='Avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
