# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-06 13:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScientificModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text=b'short descriptive name', max_length=200)),
                ('description', models.TextField()),
                ('species', models.CharField(blank=True, choices=[(b'mouse', b'Mouse (Mus musculus)'), (b'rat', b'Rat (Rattus rattus)'), (b'marmoset', b'Marmoset (callithrix jacchus)'), (b'human', b'Human (Homo sapiens)'), (b'rhesus_monkey', b'Paxinos Rhesus Monkey (Macaca mulatta)'), (b'opossum', b'Opossum (Monodelphis domestica)'), (b'other', b'Other')], help_text=b'species', max_length=100)),
                ('brain_region', models.CharField(blank=True, choices=[(b'basal ganglia', b'Basal Ganglia'), (b'cerebellum', b'Cerebellum'), (b'cortex', b'Cortex'), (b'hippocampus', b'Hippocampus'), (b'other', b'Other')], help_text=b'brain region, if applicable', max_length=100)),
                ('cell_type', models.CharField(blank=True, choices=[(b'granule cell', b'Granule Cell'), (b'interneuron', b'Interneuron'), (b'pyramidal cell', b'Pyramidal Cell'), (b'other', b'Other')], help_text=b'cell type, for single-cell models', max_length=100)),
                ('author', models.TextField(help_text=b'Author(s) of this model')),
                ('source', models.URLField(help_text=b'Version control repository containing the source code of the model')),
            ],
        ),
        migrations.CreateModel(
            name='ScientificModelInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=64)),
                ('parameters', models.TextField(blank=True, null=True)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instances', to='model_validation_api.ScientificModel')),
            ],
        ),
        migrations.CreateModel(
            name='ValidationTestCode',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('repository', models.CharField(help_text=b'location of the code that defines the test', max_length=200)),
                ('version', models.CharField(help_text=b'version of the code that defines the test', max_length=128)),
                ('path', models.CharField(help_text=b'path to test class within Python code', max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True, help_text=b'timestamp for this version of the code')),
            ],
            options={
                'get_latest_by': 'timestamp',
                'verbose_name_plural': 'validation test code',
            },
        ),
        migrations.CreateModel(
            name='ValidationTestDefinition',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text=b'short descriptive name', max_length=200)),
                ('species', models.CharField(choices=[(b'mouse', b'Mouse (Mus musculus)'), (b'rat', b'Rat (Rattus rattus)'), (b'marmoset', b'Marmoset (callithrix jacchus)'), (b'human', b'Human (Homo sapiens)'), (b'rhesus_monkey', b'Paxinos Rhesus Monkey (Macaca mulatta)'), (b'opossum', b'Opossum (Monodelphis domestica)'), (b'other', b'Other')], help_text=b'species', max_length=100)),
                ('brain_region', models.CharField(choices=[(b'basal ganglia', b'Basal Ganglia'), (b'cerebellum', b'Cerebellum'), (b'cortex', b'Cortex'), (b'hippocampus', b'Hippocampus'), (b'other', b'Other')], help_text=b'brain region', max_length=100)),
                ('cell_type', models.CharField(choices=[(b'granule cell', b'Granule Cell'), (b'interneuron', b'Interneuron'), (b'pyramidal cell', b'Pyramidal Cell'), (b'other', b'Other')], help_text=b'cell type', max_length=100)),
                ('age', models.CharField(help_text=b"age of animal, e.g. '6 weeks'", max_length=50, null=True)),
                ('data_location', models.CharField(help_text=b'location of comparison data', max_length=200)),
                ('data_type', models.CharField(help_text=b'type of comparison data (number, histogram, time series, etc.)', max_length=100)),
                ('data_modality', models.CharField(choices=[(b'ephys', b'electrophysiology'), (b'fMRI', b'fMRI'), (b'2-photon', b'2-photon imaging'), (b'em', b'electron microscopy'), (b'histology', b'histology')], help_text=b'recording modality for comparison data (ephys, fMRI, 2-photon, etc)', max_length=100)),
                ('test_type', models.CharField(choices=[(b'single cell', b'single cell activity'), (b'network structure', b'network structure'), (b'network activity', b'network activity'), (b'behaviour', b'behaviour'), (b'subcellular', b'subcellular')], help_text=b'single cell activity, network structure, network activity, subcellular', max_length=100)),
                ('protocol', models.TextField(blank=True, help_text=b'Description of the experimental protocol')),
                ('author', models.CharField(help_text=b'Author of this test', max_length=100)),
                ('publication', models.CharField(help_text=b'Publication in which the validation data set was reported', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ValidationTestResult',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('results_storage', models.TextField(help_text=b'Location of data files produced by the test run')),
                ('result', models.FloatField(help_text=b'A numerical measure of the difference between model and experiment')),
                ('passed', models.NullBooleanField(help_text=b'Whether the test passed or failed')),
                ('timestamp', models.DateTimeField(auto_now_add=True, help_text=b'Timestamp of when the simulation was run')),
                ('platform', models.TextField(help_text=b'Computer system on which the simulation was run')),
                ('project', models.CharField(blank=True, help_text=b'Project with which this test run is associated(optional)', max_length=200)),
                ('model_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model_validation_api.ScientificModelInstance')),
                ('test_definition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model_validation_api.ValidationTestCode')),
            ],
            options={
                'get_latest_by': 'timestamp',
            },
        ),
        migrations.AddField(
            model_name='validationtestcode',
            name='test_definition',
            field=models.ForeignKey(help_text=b'Validation test implemented by this code', on_delete=django.db.models.deletion.CASCADE, related_name='code', to='model_validation_api.ValidationTestDefinition'),
        ),
    ]
