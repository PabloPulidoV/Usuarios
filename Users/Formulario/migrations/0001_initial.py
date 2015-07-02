# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=40)),
                ('codigo', models.CharField(max_length=40)),
                ('edad', models.CharField(max_length=40)),
                ('contrasena', models.CharField(max_length=40)),
                ('correo', models.CharField(max_length=40)),
                ('paginaweb', models.CharField(max_length=40)),
            ],
        ),
    ]
