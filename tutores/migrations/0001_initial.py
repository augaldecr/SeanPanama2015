# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Libro'
        db.create_table(u'tutores_libro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('precio', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'tutores', ['Libro'])

        # Adding model 'Nivel'
        db.create_table(u'tutores_nivel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nivel', self.gf('django.db.models.fields.CharField')(max_length=35)),
        ))
        db.send_create_signal(u'tutores', ['Nivel'])

        # Adding M2M table for field libros on 'Nivel'
        m2m_table_name = db.shorten_name(u'tutores_nivel_libros')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('nivel', models.ForeignKey(orm[u'tutores.nivel'], null=False)),
            ('libro', models.ForeignKey(orm[u'tutores.libro'], null=False))
        ))
        db.create_unique(m2m_table_name, ['nivel_id', 'libro_id'])

        # Adding model 'Provincia'
        db.create_table(u'tutores_provincia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'tutores', ['Provincia'])

        # Adding model 'Distrito'
        db.create_table(u'tutores_distrito', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('provincia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tutores.Provincia'])),
        ))
        db.send_create_signal(u'tutores', ['Distrito'])

        # Adding model 'Denominacion'
        db.create_table(u'tutores_denominacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('usuario_publicador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'tutores', ['Denominacion'])

        # Adding model 'Centro'
        db.create_table(u'tutores_centro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('denominacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tutores.Denominacion'])),
            ('distrito', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tutores.Distrito'])),
            ('ciudad', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('usuario_publicador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'tutores', ['Centro'])

        # Adding model 'Estudiante'
        db.create_table(u'tutores_estudiante', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('centro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tutores.Centro'])),
            ('usuario_publicador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'tutores', ['Estudiante'])

        # Adding model 'Calificacion'
        db.create_table(u'tutores_calificacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estudiante', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tutores.Estudiante'])),
            ('nota', self.gf('django.db.models.fields.FloatField')()),
            ('libro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tutores.Libro'])),
            ('tutor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'tutores', ['Calificacion'])


    def backwards(self, orm):
        # Deleting model 'Libro'
        db.delete_table(u'tutores_libro')

        # Deleting model 'Nivel'
        db.delete_table(u'tutores_nivel')

        # Removing M2M table for field libros on 'Nivel'
        db.delete_table(db.shorten_name(u'tutores_nivel_libros'))

        # Deleting model 'Provincia'
        db.delete_table(u'tutores_provincia')

        # Deleting model 'Distrito'
        db.delete_table(u'tutores_distrito')

        # Deleting model 'Denominacion'
        db.delete_table(u'tutores_denominacion')

        # Deleting model 'Centro'
        db.delete_table(u'tutores_centro')

        # Deleting model 'Estudiante'
        db.delete_table(u'tutores_estudiante')

        # Deleting model 'Calificacion'
        db.delete_table(u'tutores_calificacion')


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
        u'tutores.calificacion': {
            'Meta': {'object_name': 'Calificacion'},
            'estudiante': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tutores.Estudiante']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'libro': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tutores.Libro']"}),
            'nota': ('django.db.models.fields.FloatField', [], {}),
            'tutor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'tutores.centro': {
            'Meta': {'object_name': 'Centro'},
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'denominacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tutores.Denominacion']"}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'distrito': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tutores.Distrito']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'usuario_publicador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'tutores.denominacion': {
            'Meta': {'object_name': 'Denominacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'usuario_publicador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'tutores.distrito': {
            'Meta': {'object_name': 'Distrito'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'provincia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tutores.Provincia']"})
        },
        u'tutores.estudiante': {
            'Meta': {'object_name': 'Estudiante'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'centro': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tutores.Centro']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'usuario_publicador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'tutores.libro': {
            'Meta': {'object_name': 'Libro'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'precio': ('django.db.models.fields.FloatField', [], {})
        },
        u'tutores.nivel': {
            'Meta': {'object_name': 'Nivel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'libros': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tutores.Libro']", 'symmetrical': 'False'}),
            'nivel': ('django.db.models.fields.CharField', [], {'max_length': '35'})
        },
        u'tutores.provincia': {
            'Meta': {'object_name': 'Provincia'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['tutores']