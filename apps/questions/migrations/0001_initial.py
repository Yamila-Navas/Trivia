# Generated by Django 4.2.4 on 2024-04-06 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ask', models.CharField(max_length=300, unique=True)),
                ('option_one', models.CharField(max_length=500)),
                ('option_two', models.CharField(max_length=500)),
                ('option_three', models.CharField(max_length=500)),
                ('correct_answer', models.CharField(max_length=500)),
                ('registered', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]
