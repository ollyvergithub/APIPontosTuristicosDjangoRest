# Generated by Django 2.0.4 on 2020-07-08 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0002_auto_20200708_1534'),
        ('core', '0003_pontoturistico_atracoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='comentarios',
            field=models.ManyToManyField(to='comentarios.Comentario'),
        ),
    ]