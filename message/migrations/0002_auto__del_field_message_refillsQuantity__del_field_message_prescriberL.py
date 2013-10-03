# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Message.refillsQuantity'
        db.delete_column(u'message_message', 'refillsQuantity')

        # Deleting field 'Message.prescriberLastName'
        db.delete_column(u'message_message', 'prescriberLastName')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Message.refillsQuantity'
        raise RuntimeError("Cannot reverse this migration. 'Message.refillsQuantity' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Message.refillsQuantity'
        db.add_column(u'message_message', 'refillsQuantity',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Message.prescriberLastName'
        raise RuntimeError("Cannot reverse this migration. 'Message.prescriberLastName' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Message.prescriberLastName'
        db.add_column(u'message_message', 'prescriberLastName',
                      self.gf('django.db.models.fields.CharField')(max_length=75),
                      keep_default=False)


    models = {
        u'message.message': {
            'Meta': {'object_name': 'Message'},
            'messageID': ('django.db.models.fields.CharField', [], {'max_length': '200', 'primary_key': 'True'}),
            'patientDob': ('django.db.models.fields.DateField', [], {}),
            'patientGender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'productCode': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'writtenDate': ('django.db.models.fields.DateField', [], {}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['message']