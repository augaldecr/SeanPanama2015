# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Noticia'
        db.create_table(u'sean_noticia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('contenido', self.gf('django.db.models.fields.TextField')(max_length=300)),
            ('fecha_publicacion', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('usuario_publicador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'sean', ['Noticia'])

        # Adding model 'Comentario'
        db.create_table(u'sean_comentario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contenido', self.gf('django.db.models.fields.TextField')(max_length=140)),
            ('comentador', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('comentador_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('noticia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sean.Noticia'])),
            ('fecha_comentario', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('aprobacion', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'sean', ['Comentario'])

        # Adding model 'Libro'
        db.create_table(u'sean_libro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=350)),
            ('portada', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'sean', ['Libro'])

        # Adding model 'Nivel'
        db.create_table(u'sean_nivel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nivel', self.gf('django.db.models.fields.CharField')(max_length=35)),
        ))
        db.send_create_signal(u'sean', ['Nivel'])

        # Adding M2M table for field libros on 'Nivel'
        m2m_table_name = db.shorten_name(u'sean_nivel_libros')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('nivel', models.ForeignKey(orm[u'sean.nivel'], null=False)),
            ('libro', models.ForeignKey(orm[u'sean.libro'], null=False))
        ))
        db.create_unique(m2m_table_name, ['nivel_id', 'libro_id'])

        # Adding model 'Mensaje'
        db.create_table(u'sean_mensaje', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('mensaje', self.gf('django.db.models.fields.TextField')(max_length=300)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('usuario_publicador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'sean', ['Mensaje'])


    def backwards(self, orm):
        # Deleting model 'Noticia'
        db.delete_table(u'sean_noticia')

        # Deleting model 'Comentario'
        db.delete_table(u'sean_comentario')

        # Deleting model 'Libro'
        db.delete_table(u'sean_libro')

        # Deleting model 'Nivel'
        db.delete_table(u'sean_nivel')

        # Removing M2M table for field libros on 'Nivel'
        db.delete_table(db.shorten_name(u'sean_nivel_libros'))

        # Deleting model 'Mensaje'
        db.delete_table(u'sean_mensaje')


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
        u'sean.comentario': {
            'Meta': {'object_name': 'Comentario'},
            'aprobacion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comentador': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'comentador_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'contenido': ('django.db.models.fields.TextField', [], {'max_length': '140'}),
            'fecha_comentario': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'noticia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sean.Noticia']"})
        },
        u'sean.libro': {
            'Meta': {'object_name': 'Libro'},
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '350'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'portada': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'sean.mensaje': {
            'Meta': {'object_name': 'Mensaje'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mensaje': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'usuario_publicador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'sean.nivel': {
            'Meta': {'object_name': 'Nivel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'libros': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['sean.Libro']", 'symmetrical': 'False'}),
            'nivel': ('django.db.models.fields.CharField', [], {'max_length': '35'})
        },
        u'sean.noticia': {
            'Meta': {'object_name': 'Noticia'},
            'contenido': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'fecha_publicacion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'usuario_publicador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['sean']