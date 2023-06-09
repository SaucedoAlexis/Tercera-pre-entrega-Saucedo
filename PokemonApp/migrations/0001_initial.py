# Generated by Django 4.1.7 on 2023-03-11 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrenador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('genero', models.CharField(max_length=10)),
                ('region', models.CharField(max_length=40)),
                ('clase', models.CharField(max_length=40)),
                ('url_img', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('tipo1', models.CharField(max_length=40)),
                ('tipo2', models.CharField(max_length=40)),
                ('url_img', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profesor', models.CharField(max_length=40)),
                ('villanos', models.CharField(max_length=40)),
                ('capital', models.CharField(max_length=40)),
                ('liga_pokemon', models.CharField(max_length=40)),
            ],
        ),
    ]
