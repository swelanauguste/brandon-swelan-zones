# Generated by Django 4.0.4 on 2022-05-18 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zones', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agency',
            name='zone',
        ),
        migrations.AddField(
            model_name='zone',
            name='zone',
            field=models.ManyToManyField(related_name='agencies', to='zones.agency'),
        ),
    ]
