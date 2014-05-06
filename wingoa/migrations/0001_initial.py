# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Department'
        db.create_table(u'wingoa_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'wingoa', ['Department'])

        # Adding model 'Position'
        db.create_table(u'wingoa_position', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'wingoa', ['Position'])

        # Adding model 'Rank'
        db.create_table(u'wingoa_rank', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'wingoa', ['Rank'])

        # Adding model 'Staff'
        db.create_table(u'wingoa_staff', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('sex', self.gf('django.db.models.fields.CharField')(default='F', max_length=2)),
            ('sid', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('birthday', self.gf('django.db.models.fields.DateField')()),
            ('graduate', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('major', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('wid', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('datentry', self.gf('django.db.models.fields.DateField')()),
            ('datexpire', self.gf('django.db.models.fields.DateField')()),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('rank', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'wingoa', ['Staff'])


    def backwards(self, orm):
        # Deleting model 'Department'
        db.delete_table(u'wingoa_department')

        # Deleting model 'Position'
        db.delete_table(u'wingoa_position')

        # Deleting model 'Rank'
        db.delete_table(u'wingoa_rank')

        # Deleting model 'Staff'
        db.delete_table(u'wingoa_staff')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'wingoa.department': {
            'Meta': {'object_name': 'Department'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'wingoa.position': {
            'Meta': {'object_name': 'Position'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'wingoa.rank': {
            'Meta': {'object_name': 'Rank'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'wingoa.staff': {
            'Meta': {'ordering': "['datentry']", 'object_name': 'Staff'},
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'datentry': ('django.db.models.fields.DateField', [], {}),
            'datexpire': ('django.db.models.fields.DateField', [], {}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'graduate': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'major': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'rank': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'sex': ('django.db.models.fields.CharField', [], {'default': "'F'", 'max_length': '2'}),
            'sid': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'wid': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        }
    }

    complete_apps = ['wingoa']