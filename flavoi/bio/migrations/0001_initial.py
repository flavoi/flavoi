# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=30)),
                ('subtitle', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to=b'/media/profile_pic/', blank=True)),
                ('cv', models.FileField(upload_to=b'/media/curriculum_vitae', blank=True)),
                ('job_content', models.TextField(blank=True)),
                ('hobby_content', models.TextField(blank=True)),
                ('dummy', models.IntegerField()),
                ('email', models.EmailField(max_length=75)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(max_length=255, blank=True)),
                ('label', models.CharField(max_length=30)),
                ('link', models.URLField()),
                ('icon', models.SlugField(max_length=30)),
                ('primary', models.BooleanField(default=True)),
                ('bio', models.ForeignKey(to='bio.Bio')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Inspiration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quote', models.TextField(max_length=255)),
                ('author', models.CharField(max_length=30)),
                ('bio', models.ForeignKey(to='bio.Bio')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
