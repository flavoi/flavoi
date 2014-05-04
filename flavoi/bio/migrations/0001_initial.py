# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Bio'
        db.create_table(u'bio_bio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('subtitle', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('cv', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(max_length=255, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'bio', ['Bio'])

        # Adding model 'Contact'
        db.create_table(u'bio_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bio.Bio'])),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=255, blank=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('icon', self.gf('django.db.models.fields.SlugField')(max_length=30)),
        ))
        db.send_create_signal(u'bio', ['Contact'])

        # Adding model 'Inspiration'
        db.create_table(u'bio_inspiration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bio.Bio'])),
            ('quote', self.gf('django.db.models.fields.TextField')(max_length=255)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'bio', ['Inspiration'])


    def backwards(self, orm):
        # Deleting model 'Bio'
        db.delete_table(u'bio_bio')

        # Deleting model 'Contact'
        db.delete_table(u'bio_contact')

        # Deleting model 'Inspiration'
        db.delete_table(u'bio_inspiration')


    models = {
        u'bio.bio': {
            'Meta': {'object_name': 'Bio'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'max_length': '255', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cv': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'bio.contact': {
            'Meta': {'object_name': 'Contact'},
            'bio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bio.Bio']"}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '255', 'blank': 'True'}),
            'icon': ('django.db.models.fields.SlugField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'bio.inspiration': {
            'Meta': {'object_name': 'Inspiration'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'bio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bio.Bio']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quote': ('django.db.models.fields.TextField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['bio']