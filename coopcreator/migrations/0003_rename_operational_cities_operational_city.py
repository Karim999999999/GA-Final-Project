# Generated by Django 4.0.4 on 2022-04-19 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coopcreator', '0002_operational_cities_remove_cooptag_description_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Operational_Cities',
            new_name='Operational_City',
        ),
    ]