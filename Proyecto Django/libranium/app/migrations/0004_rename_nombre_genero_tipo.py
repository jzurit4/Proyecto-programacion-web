# Generated by Django 4.1.2 on 2024-06-30 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_contacto_alter_genero_nombre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genero',
            old_name='nombre',
            new_name='tipo',
        ),
    ]
