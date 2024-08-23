# Generated by Django 4.1 on 2024-08-23 08:56

import cinema.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(null=True, upload_to=cinema.models.generate_movie_image_path),
        ),
    ]
