# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 08:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GalaxyInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url', models.URLField(help_text='Instance URL', null=True)),
                ('title', models.CharField(help_text='The name / title of the instance. E.g. GalaxyP', max_length=256, null=True)),
                ('description', models.TextField(help_text='Any extra description you wish to add.', null=True)),
                ('users_recent', models.IntegerField(default=0)),
                ('users_total', models.IntegerField(default=0)),
                ('jobs_run', models.IntegerField(default=0)),
                ('api_key', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('last_import', models.FloatField(default=-1)),
                ('owners', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_job_id', models.IntegerField(default=-1)),
                ('tool_id', models.CharField(max_length=255)),
                ('tool_version', models.TextField()),
                ('state', models.CharField(max_length=16)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.GalaxyInstance')),
            ],
        ),
        migrations.CreateModel(
            name='JobParam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('value', models.TextField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Job')),
            ],
        ),
        migrations.CreateModel(
            name='MetricNumeric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plugin', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=256)),
                ('value', models.DecimalField(decimal_places=7, max_digits=22)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Job')),
            ],
        ),
        migrations.CreateModel(
            name='MetricText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plugin', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=256)),
                ('value', models.CharField(max_length=256)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Job')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='job',
            unique_together=set([('instance', 'external_job_id')]),
        ),
    ]
