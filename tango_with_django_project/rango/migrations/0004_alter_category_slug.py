# Generated by Django 4.1.5 on 2023-02-10 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rango", "0003_alter_category_options_category_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
