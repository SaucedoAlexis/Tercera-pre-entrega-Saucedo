# Generated by Django 4.1 on 2023-03-16 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("PokemonApp", "0003_region_url_img_alter_pokemon_tipo2"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pokemon",
            name="tipo2",
            field=models.CharField(default=None, max_length=40),
        ),
    ]
