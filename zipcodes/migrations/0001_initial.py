# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Zipcode'
        db.create_table(u'zipcodes_zipcode', (
            ('zipcode', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('prescriberCases', self.gf('django.db.models.fields.IntegerField')()),
            ('patientCases', self.gf('django.db.models.fields.IntegerField')()),
            ('pharmacyCases', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'zipcodes', ['Zipcode'])


    def backwards(self, orm):
        # Deleting model 'Zipcode'
        db.delete_table(u'zipcodes_zipcode')


    models = {
        u'zipcodes.zipcode': {
            'Meta': {'object_name': 'Zipcode'},
            'patientCases': ('django.db.models.fields.IntegerField', [], {}),
            'pharmacyCases': ('django.db.models.fields.IntegerField', [], {}),
            'prescriberCases': ('django.db.models.fields.IntegerField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['zipcodes']