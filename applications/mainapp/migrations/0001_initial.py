# Generated by Django 3.0.5 on 2022-04-01 00:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Extorsion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreExtorsionador', models.CharField(max_length=60, verbose_name='Nombre del extorsionador')),
                ('numero', models.CharField(max_length=60, verbose_name='numero')),
                ('cuenta', models.CharField(max_length=60, verbose_name='cuenta')),
                ('deposito', models.FloatField(verbose_name='Cantidad depositado')),
            ],
            options={
                'verbose_name': 'Extorsion',
                'verbose_name_plural': 'Extorsiones',
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'Municipio',
                'verbose_name_plural': 'Municipios',
            },
        ),
        migrations.CreateModel(
            name='TipoIncidente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=60, verbose_name='Tipo')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Tipo de incidente',
                'verbose_name_plural': 'Tipos de incidentes',
            },
        ),
        migrations.CreateModel(
            name='Incidente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folio', models.CharField(max_length=50, verbose_name='Folio')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('hora', models.TimeField(max_length=50, verbose_name='Hora')),
                ('nombreAfectado', models.CharField(max_length=100, verbose_name='Nombre del afectado')),
                ('numeroAfectado', models.CharField(max_length=20, verbose_name='Numero del afectado')),
                ('descripcion', models.TextField(verbose_name='Descripcion de incidente')),
                ('resulado', models.TextField(verbose_name='Resultado del incidente')),
                ('extorsion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Extorsion', verbose_name='Extorsion')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Municipio', verbose_name='Municipio')),
                ('tipoIncidente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.TipoIncidente', verbose_name='Tipo de incidente')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Atendio')),
            ],
            options={
                'verbose_name': 'Incidente',
                'verbose_name_plural': 'Incidentes',
            },
        ),
    ]