# Generated by Django 4.1.7 on 2023-03-24 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PokemonApp', '0010_alter_pokemon_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='numero',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
