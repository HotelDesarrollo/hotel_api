# Generated by Django 4.0 on 2024-06-04 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alojamientos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=150)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('numero_personas', models.PositiveIntegerField(default=0)),
                ('estado', models.CharField(default='Disponible', max_length=17)),
                ('eliminado', models.CharField(default='NO', max_length=2)),
                ('alojamiento_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='alojamientos.alojamiento')),
            ],
            options={
                'verbose_name': 'Habitacion',
                'verbose_name_plural': 'Habitaciones',
                'db_table': 'Habitacion',
            },
        ),
    ]