# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='description',
            field=models.TextField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
