# Generated by Django 4.1.7 on 2023-03-16 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='quantEpisodios',
            field=models.IntegerField(default=0),
        ),
    ]
