# Generated by Django 4.1.7 on 2023-03-16 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0002_filme_quantepisodios'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='capaFilme',
            field=models.ImageField(default=None, upload_to='capa-filmes'),
        ),
    ]