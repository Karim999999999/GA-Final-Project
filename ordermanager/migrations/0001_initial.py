# Generated by Django 4.0.4 on 2022-04-20 16:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coopmanager', '0003_delete_shoppingbasket'),
        ('coopcreator', '0007_coop_postcode'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderProposalStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
                ('status_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
                ('status_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OrderProposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('deadline', models.DateField()),
                ('delivery_day', models.DateField()),
                ('coop_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopping_list', to='coopcreator.coop')),
                ('items_id', models.ManyToManyField(related_name='shopping_list', to='coopmanager.coopitem')),
                ('order_proposal_status', models.ManyToManyField(related_name='orders', to='ordermanager.orderproposalstatus')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_proposal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='ordermanager.orderproposal')),
                ('order_status', models.ManyToManyField(related_name='orders', to='ordermanager.orderstatus')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
