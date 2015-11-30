# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0002_goal_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'/media/goals/', blank=True),
            preserve_default=True,
        ),
    ]
