# Generated by Django 5.0.6 on 2024-06-05 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0007_rename_apellido_personal_apellido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatarPersonal/'),
        ),
    ]
