# Generated by Django 4.1.7 on 2023-03-17 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0005_remove_filme_capafilme'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='capaFilme',
            field=models.ImageField(null=True, upload_to='imagens-dos-filmes'),
        ),
    ]
