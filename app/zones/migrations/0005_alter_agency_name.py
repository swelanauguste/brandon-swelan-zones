# Generated by Django 4.0.4 on 2022-05-18 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zones', '0004_rename_zone_zone_agency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
