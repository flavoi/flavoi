# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Goal.completed'
        db.delete_column(u'goal_goal', 'completed')

        # Adding field 'Goal.percentage'
        db.add_column(u'goal_goal', 'percentage',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Goal.completed'
        db.add_column(u'goal_goal', 'completed',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'Goal.percentage'
        db.delete_column(u'goal_goal', 'percentage')


    models = {
        u'goal.goal': {
            'Meta': {'object_name': 'Goal'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'percentage': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['goal']