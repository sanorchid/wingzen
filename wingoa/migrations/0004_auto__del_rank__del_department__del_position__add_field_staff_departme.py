# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Rank'
        db.delete_table(u'wingoa_rank')

        # Deleting model 'Department'
        db.delete_table(u'wingoa_department')

        # Deleting model 'Position'
        db.delete_table(u'wingoa_position')

        # Adding field 'Staff.department'
        db.add_column(u'wingoa_staff', 'department',
                      self.gf('django.db.models.fields.CharField')(default=2010, max_length=15),
                      keep_default=False)

        # Adding field 'Staff.position'
        db.add_column(u'wingoa_staff', 'position',
                      self.gf('django.db.models.fields.CharField')(default=2010, max_length=15),
                      keep_default=False)

        # Adding field 'Staff.rank'
        db.add_column(u'wingoa_staff', 'rank',
                      self.gf('django.db.models.fields.CharField')(default=2010, max_length=10),
                      keep_default=False)

        # Removing M2M table for field rank on 'Staff'
        db.delete_table(db.shorten_name(u'wingoa_staff_rank'))

        # Removing M2M table for field department on 'Staff'
        db.delete_table(db.shorten_name(u'wingoa_staff_department'))

        # Removing M2M table for field position on 'Staff'
        db.delete_table(db.shorten_name(u'wingoa_staff_position'))


    def backwards(self, orm):
        # Adding model 'Rank'
        db.create_table(u'wingoa_rank', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='20')),
        ))
        db.send_create_signal(u'wingoa', ['Rank'])

        # Adding model 'Department'
        db.create_table(u'wingoa_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='20')),
        ))
        db.send_create_signal(u'wingoa', ['Department'])

        # Adding model 'Position'
        db.create_table(u'wingoa_position', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='20')),
        ))
        db.send_create_signal(u'wingoa', ['Position'])

        # Deleting field 'Staff.department'
        db.delete_column(u'wingoa_staff', 'department')

        # Deleting field 'Staff.position'
        db.delete_column(u'wingoa_staff', 'position')

        # Deleting field 'Staff.rank'
        db.delete_column(u'wingoa_staff', 'rank')

        # Adding M2M table for field rank on 'Staff'
        m2m_table_name = db.shorten_name(u'wingoa_staff_rank')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('staff', models.ForeignKey(orm[u'wingoa.staff'], null=False)),
            ('rank', models.ForeignKey(orm[u'wingoa.rank'], null=False))
        ))
        db.create_unique(m2m_table_name, ['staff_id', 'rank_id'])

        # Adding M2M table for field department on 'Staff'
        m2m_table_name = db.shorten_name(u'wingoa_staff_department')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('staff', models.ForeignKey(orm[u'wingoa.staff'], null=False)),
            ('department', models.ForeignKey(orm[u'wingoa.department'], null=False))
        ))
        db.create_unique(m2m_table_name, ['staff_id', 'department_id'])

        # Adding M2M table for field position on 'Staff'
        m2m_table_name = db.shorten_name(u'wingoa_staff_position')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('staff', models.ForeignKey(orm[u'wingoa.staff'], null=False)),
            ('position', models.ForeignKey(orm[u'wingoa.position'], null=False))
        ))
        db.create_unique(m2m_table_name, ['staff_id', 'position_id'])


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
        u'wingoa.staff': {
            'Meta': {'ordering': "['datentry']", 'object_name': 'Staff'},
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'datentry': ('django.db.models.fields.DateField', [], {}),
            'datexpire': ('django.db.models.fields.DateField', [], {}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'graduate': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'major': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'rank': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'sex': ('django.db.models.fields.CharField', [], {'default': "'F'", 'max_length': '2'}),
            'sid': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'wid': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        }
    }

    complete_apps = ['wingoa']