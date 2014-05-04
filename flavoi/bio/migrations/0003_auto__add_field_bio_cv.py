# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Bio.cv'
        db.add_column(u'bio_bio', 'cv',
                      self.gf('django.db.models.fields.files.FileField')(default='', max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Bio.cv'
        db.delete_column(u'bio_bio', 'cv')


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