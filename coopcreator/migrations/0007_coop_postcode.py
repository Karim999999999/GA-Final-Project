# Generated by Django 4.0.4 on 2022-04-20 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coopcreator', '0006_alter_coop_city_alter_coop_coop_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='coop',
            name='postcode',
            field=models.CharField(default='text', max_length=9),
            preserve_default=False,
        ),
    ]
