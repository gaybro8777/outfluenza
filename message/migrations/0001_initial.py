# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Message'
        db.create_table(u'message_message', (
            ('messageID', self.gf('django.db.models.fields.CharField')(max_length=200, primary_key=True)),
            ('writtenDate', self.gf('django.db.models.fields.DateField')()),
            ('productCode', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('refillsQuantity', self.gf('django.db.models.fields.IntegerField')()),
            ('patientGender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('patientDob', self.gf('django.db.models.fields.DateField')()),
            ('prescriberLastName', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('zipcode', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'message', ['Message'])


    def backwards(self, orm):
        # Deleting model 'Message'
        db.delete_table(u'message_message')


    models = {
        u'message.message': {
            'Meta': {'object_name': 'Message'},
            'messageID': ('django.db.models.fields.CharField', [], {'max_length': '200', 'primary_key': 'True'}),
            'patientDob': ('django.db.models.fields.DateField', [], {}),
            'patientGender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'prescriberLastName': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'productCode': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'refillsQuantity': ('django.db.models.fields.IntegerField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'writtenDate': ('django.db.models.fields.DateField', [], {}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['message']