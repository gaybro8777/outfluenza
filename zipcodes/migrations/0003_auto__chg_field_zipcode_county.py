# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Zipcode.county'
        db.alter_column(u'zipcodes_zipcode', 'county', self.gf('django.db.models.fields.CharField')(max_length=100))

    def backwards(self, orm):

        # Changing field 'Zipcode.county'
        db.alter_column(u'zipcodes_zipcode', 'county', self.gf('django.db.models.fields.CharField')(max_length=20))

    models = {
        u'zipcodes.zipcode': {
            'Meta': {'object_name': 'Zipcode'},
            'county': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'femalePatientCases': ('django.db.models.fields.IntegerField', [], {}),
            'malePatientCases': ('django.db.models.fields.IntegerField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['zipcodes']