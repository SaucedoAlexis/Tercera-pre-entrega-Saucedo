# Generated by Django 4.1 on 2023-03-16 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("PokemonApp", "0005_region_nombre"),
    ]

    operations = [
        migrations.AlterField(
            model_name="region",
            name="nombre",
            field=models.CharField(default=True, max_length=40),
        ),
        migrations.AlterField(
            model_name="region", name="url_img", field=models.URLField(default=True),
        ),
    ]
