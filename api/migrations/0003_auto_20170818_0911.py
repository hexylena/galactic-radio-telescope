# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-18 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_galaxyinstance_jobs_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='external_job_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='jobparam',
            name='external_job_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='jobparam',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='metricnumeric',
            name='external_job_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='metricnumeric',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='metrictext',
            name='external_job_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='metrictext',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]