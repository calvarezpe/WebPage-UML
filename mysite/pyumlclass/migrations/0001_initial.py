# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-10 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=200)),
                ('uml_class', models.IntegerField(default=0)),
                ('python_class', models.IntegerField(default=0)),
                ('intersection', models.IntegerField(default=0)),
                ('without_corrections', models.IntegerField(default=0)),
                ('hamming_corrections', models.IntegerField(default=0)),
                ('capital_letters_corrections', models.IntegerField(default=0)),
            ],
        ),
    ]
