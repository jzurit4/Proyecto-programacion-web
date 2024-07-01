# Generated by Django 5.0.1 on 2024-07-01 13:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('año_pub', models.CharField(max_length=4)),
                ('editorial', models.CharField(max_length=50)),
                ('encuadernacion', models.CharField(max_length=50)),
                ('imagen', models.ImageField(null=True, upload_to='libros')),
            ],
        ),
        migrations.RemoveField(
            model_name='producto',
            name='genero',
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('titulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.libro')),
            ],
        ),
        migrations.DeleteModel(
            name='Genero',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]