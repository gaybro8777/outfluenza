# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Zipcode.prescriberCases'
        db.delete_column(u'zipcodes_zipcode', 'prescriberCases')

        # Deleting field 'Zipcode.patientCases'
        db.delete_column(u'zipcodes_zipcode', 'patientCases')

        # Deleting field 'Zipcode.pharmacyCases'
        db.delete_column(u'zipcodes_zipcode', 'pharmacyCases')

        # Adding field 'Zipcode.county'
        db.add_column(u'zipcodes_zipcode', 'county',
                      self.gf('django.db.models.fields.CharField')(default='NA', max_length=20),
                      keep_default=False)

        # Adding field 'Zipcode.malePatientCases'
        db.add_column(u'zipcodes_zipcode', 'malePatientCases',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Zipcode.femalePatientCases'
        db.add_column(u'zipcodes_zipcode', 'femalePatientCases',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Zipcode.prescriberCases'
        raise RuntimeError("Cannot reverse this migration. 'Zipcode.prescriberCases' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Zipcode.prescriberCases'
        db.add_column(u'zipcodes_zipcode', 'prescriberCases',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Zipcode.patientCases'
        raise RuntimeError("Cannot reverse this migration. 'Zipcode.patientCases' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Zipcode.patientCases'
        db.add_column(u'zipcodes_zipcode', 'patientCases',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Zipcode.pharmacyCases'
        raise RuntimeError("Cannot reverse this migration. 'Zipcode.pharmacyCases' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Zipcode.pharmacyCases'
        db.add_column(u'zipcodes_zipcode', 'pharmacyCases',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)

        # Deleting field 'Zipcode.county'
        db.delete_column(u'zipcodes_zipcode', 'county')

        # Deleting field 'Zipcode.malePatientCases'
        db.delete_column(u'zipcodes_zipcode', 'malePatientCases')

        # Deleting field 'Zipcode.femalePatientCases'
        db.delete_column(u'zipcodes_zipcode', 'femalePatientCases')


    models = {
        u'zipcodes.zipcode': {
            'Meta': {'object_name': 'Zipcode'},
            'county': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'femalePatientCases': ('django.db.models.fields.IntegerField', [], {}),
            'malePatientCases': ('django.db.models.fields.IntegerField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['zipcodes']