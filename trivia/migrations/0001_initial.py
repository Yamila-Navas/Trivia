# Generated by Django 4.2.7 on 2023-11-29 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=100)),
                ('url_api', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Trivia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jugador', models.CharField(max_length=20)),
                ('tiempo_inicial', models.DateTimeField(auto_now_add=True)),
                ('tiempo_final', models.DateTimeField(blank=True, null=True)),
                ('aciertos', models.PositiveIntegerField(default=0)),
                ('categoria', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='trivia.categorias')),
            ],
        ),
    ]
