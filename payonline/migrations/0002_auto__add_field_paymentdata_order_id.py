# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PaymentData.order_id'
        db.add_column(u'payonline_paymentdata', 'order_id',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PaymentData.order_id'
        db.delete_column(u'payonline_paymentdata', 'order_id')


    models = {
        u'payonline.paymentdata': {
            'Meta': {'object_name': 'PaymentData'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'bin_country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'card_holder': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'card_number': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ip_country': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'order_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'provider': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'transaction_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'wm_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'wm_inv_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wm_purse': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'wm_tran_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['payonline']