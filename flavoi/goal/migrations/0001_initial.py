# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=60)),
                ('published', models.BooleanField(default=False)),
                ('percentage', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100)])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
