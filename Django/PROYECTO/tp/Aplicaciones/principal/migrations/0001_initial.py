# Generated by Django 3.1.4 on 2021-02-19 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=70, unique=True)),
                ('duracion', models.IntegerField()),
                ('descripcion', models.CharField(default=False, max_length=200)),
                ('detalle', models.CharField(max_length=200)),
                ('genero', models.CharField(max_length=30)),
                ('clasificacion', models.CharField(max_length=5)),
                ('estado', models.BooleanField(default=False)),
                ('fechaComienzo', models.DateTimeField()),
                ('fechaFinalizacion', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Proyeccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('hora', models.TimeField()),
                ('estado', models.BooleanField(default=False)),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.pelicula')),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=70)),
                ('estado', models.BooleanField(default=False)),
                ('filas', models.IntegerField()),
                ('asientos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('filas', models.IntegerField()),
                ('asientos', models.IntegerField()),
                ('proyeccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.proyeccion')),
            ],
        ),
        migrations.AddField(
            model_name='proyeccion',
            name='sala',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.sala'),
        ),
    ]
