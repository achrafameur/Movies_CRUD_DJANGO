# Generated by Django 5.0.6 on 2024-06-12 19:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_service', '0004_movie_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='duration',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='hasReservationsAvailable',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='rate',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
