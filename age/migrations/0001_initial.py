# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Age'
        db.create_table(u'age_age', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('age', self.gf('django.db.models.fields.IntegerField')()),
            ('num_cases', self.gf('django.db.models.fields.IntegerField')()),
            ('zipcode', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'age', ['Age'])


    def backwards(self, orm):
        # Deleting model 'Age'
        db.delete_table(u'age_age')


    models = {
        u'age.age': {
            'Meta': {'object_name': 'Age'},
            'age': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_cases': ('django.db.models.fields.IntegerField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['age']