# Generated by Django 4.0.4 on 2022-05-18 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zones', '0006_alter_agency_common_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agency',
            options={'ordering': ('common_name',), 'verbose_name_plural': 'Agencies'},
        ),
    ]
