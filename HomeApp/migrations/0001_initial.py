# Generated by Django 3.0.4 on 2020-05-12 05:13

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('responsavel', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Toner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
                ('referencia', models.CharField(max_length=200)),
                ('cor', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Saida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_saida', models.IntegerField(default=0, editable=False)),
                ('data_saida', models.DateField(default=datetime.datetime(2020, 5, 12, 5, 13, 2, 418099, tzinfo=utc))),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeApp.Departamento')),
                ('descricao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeApp.Toner')),
            ],
            options={
                'ordering': ['descricao'],
            },
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_entrada', models.IntegerField(default=1, editable=False)),
                ('data', models.DateTimeField(default=datetime.datetime(2020, 5, 12, 5, 13, 2, 417596, tzinfo=utc))),
                ('descricao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeApp.Toner')),
            ],
            options={
                'ordering': ['descricao'],
            },
        ),
    ]
