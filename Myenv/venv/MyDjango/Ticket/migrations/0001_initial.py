# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('user_name', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=16)),
                ('full_name', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('auth_type', models.IntegerField()),
            ],
        ),
    ]
