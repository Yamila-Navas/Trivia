# Generated by Django 4.2.7 on 2024-03-09 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0005_alter_trivia_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trivia',
            name='tiempo_final',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
