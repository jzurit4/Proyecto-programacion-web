# Generated by Django 5.0 on 2024-06-24 13:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('autor', models.CharField(max_length=50)),
                ('sinopsis', models.TextField()),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.genero')),
            ],
        ),
    ]
