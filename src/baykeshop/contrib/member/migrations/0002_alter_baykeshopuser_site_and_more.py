# Generated by Django 5.1.4 on 2024-12-04 17:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baykeshopuser',
            name='site',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site', verbose_name='站点'),
        ),
        migrations.AlterField(
            model_name='baykeshopuseraddress',
            name='site',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site', verbose_name='站点'),
        ),
    ]